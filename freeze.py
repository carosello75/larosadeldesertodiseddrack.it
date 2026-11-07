"""Genera il sito statico in ./build per GitHub Pages.

Uso:  python freeze.py
Flask serve solo a costruire le pagine: online va HTML/CSS/JS puro, velocissimo e senza server.
"""
import re
import shutil
import sys
from pathlib import Path
from xml.etree import ElementTree

from app import create_app
from app.routes import OLD_CATEGORIES, OLD_PAGES

DOMAIN = "larosadeldesertodiseddrack.it"
OUT = Path(__file__).parent / "build"

REDIRECT_PAGE = """<!doctype html><html lang="it"><head><meta charset="utf-8">
<title>Pagina spostata</title><meta name="robots" content="noindex">
<link rel="canonical" href="{abs}"><meta http-equiv="refresh" content="0; url={to}">
</head><body><p>Questa pagina si è spostata: <a href="{to}">{to}</a></p></body></html>"""


def write(path, data):
    target = OUT / path.lstrip("/")
    if path.endswith("/"):
        target = target / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def main():
    app = create_app()
    site = app.config["SITE_URL"]
    client = app.test_client()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    sitemap = client.get("/sitemap.xml").data
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    pages = [u.text.replace(site, "") for u in ElementTree.fromstring(sitemap).findall(".//s:loc", ns)]
    pages += ["/cookie-policy/", "/privacy/"]

    errors = 0
    for url in pages:
        r = client.get(url)
        if r.status_code != 200:
            print("ERRORE", r.status_code, url); errors += 1; continue
        write(url, r.data)
    write("/sitemap.xml", sitemap)
    write("/robots.txt", client.get("/robots.txt").data)
    write("/manifest.webmanifest", client.get("/manifest.webmanifest").data)
    write("/sw.js", client.get("/sw.js").data)
    write("/offline/", client.get("/offline/").data)
    write("/404.html", client.get("/__pagina-inesistente__/").data)

    # Vecchi indirizzi WordPress -> pagine di reindirizzamento
    old = [f"/{p}/" for p in OLD_PAGES] + [f"/category/{c}/" for c in OLD_CATEGORIES] + ["/per-natale/", "/feed/"]
    old += [f"/{p['date'][:4]}/{p['date'][5:7]}/{p['date'][8:10]}/{p['slug']}/" for p in app.config["POSTS"]]
    for url in old:
        r = client.get(url)
        to = r.headers.get("Location", "/")
        to = re.sub(r"^https?://[^/]+", "", to)
        write(url, REDIRECT_PAGE.format(to=to, abs=site + to).encode())

    shutil.copytree(Path(app.static_folder), OUT / "static")
    (OUT / "CNAME").write_text(DOMAIN + "\n")
    (OUT / ".nojekyll").write_text("")
    print(f"Pagine: {len(pages)}  redirect: {len(old)}  errori: {errors}  -> {OUT}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
