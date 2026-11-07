import json
import re

import pytest

from app import create_app
from app.site_data import LOCATIONS, SERVICES


@pytest.fixture()
def client():
    return create_app({"TESTING": True}).test_client()


def all_pages(client):
    xml = client.get("/sitemap.xml").data.decode()
    return [u.split(".it", 1)[1] for u in re.findall(r"<loc>([^<]+)</loc>", xml)]


def test_every_page_renders(client):
    pages = all_pages(client)
    assert len(pages) >= 20
    for url in pages:
        r = client.get(url)
        assert r.status_code == 200, url
        html = r.data.decode()
        assert "<h1" in html, url
        assert "tel:+393899962511" in html, url


def test_structured_data_has_two_florists(client):
    html = client.get("/").data.decode()
    data = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1))
    florists = [n for n in data["@graph"] if n["@type"] == "Florist"]
    assert {f["address"]["postalCode"] for f in florists} == {"00179", "00147"}
    assert len({f["@id"] for f in florists}) == 2


def test_disambiguation_notice_everywhere(client):
    for url in ("/", "/contatti/", "/fioraio-largo-santi-martiri-uganda/"):
        assert "Non abbiamo legami con ristoranti" in client.get(url).data.decode()


def test_old_wordpress_urls_redirect(client):
    assert client.get("/la-nostra-gallery/").headers["Location"].endswith("/galleria/")
    assert client.get("/2024/11/10/addobbi-matrimoniali-roma/").headers["Location"].endswith("/blog/addobbi-matrimoniali-roma/")
    assert client.get("/category/largo-santi-martiri-delluganda-roma/").headers["Location"].endswith("/fioraio-largo-santi-martiri-uganda/")


def test_images_referenced_exist(client):
    from pathlib import Path
    static = Path(__file__).parents[1] / "app" / "static"
    for url in all_pages(client):
        for src in re.findall(r'src="(/static/[^"?]+)', client.get(url).data.decode()):
            assert (static / src[len("/static/"):]).exists(), (url, src)


def test_no_tracking_without_tag(client):
    assert "googletagmanager" not in client.get("/").data.decode()


def test_tracking_with_tag():
    c = create_app({"TESTING": True, "GOOGLE_TAG_ID": "AW-123"}).test_client()
    html = c.get("/").data.decode()
    assert "AW-123" in html and "'consent', 'default'" in html


def test_404(client):
    assert client.get("/non-esiste/").status_code == 404


def test_booking_page_posts_to_owner_email(client):
    html = client.get("/prenota/").data.decode()
    assert 'action="https://formsubmit.co/ajax/larosadeldesertoseddrak@gmail.com"' in html
    for field in ("Nome", "Cognome", "email", "Telefono", "Indirizzo", "Data"):
        assert f'name="{field}"' in html


def test_pwa_files(client):
    m = json.loads(client.get("/manifest.webmanifest").data)
    assert m["display"] == "standalone" and len(m["icons"]) == 3
    assert b"serviceWorker" not in client.get("/sw.js").data  # è il worker, non il registratore
    assert 'rel="manifest"' in client.get("/").data.decode()


def test_iban_is_valid_and_shown(client):
    from app.site_data import BUSINESS
    iban = BUSINESS["iban"].replace(" ", "")
    assert int("".join(str(int(c, 36)) for c in iban[4:] + iban[:4])) % 97 == 1
    html = client.get("/pagamento/").data.decode()
    assert BUSINESS["iban"] in html and BUSINESS["iban_holder"] in html
