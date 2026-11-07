import json
from datetime import date

from flask import current_app, request, url_for
from markupsafe import Markup, escape

from .site_data import BUSINESS, LOCATIONS, NAV, SERVICES

DAYS_IT = {
    "Monday": "Lunedì", "Tuesday": "Martedì", "Wednesday": "Mercoledì", "Thursday": "Giovedì",
    "Friday": "Venerdì", "Saturday": "Sabato", "Sunday": "Domenica",
}
MONTHS_IT = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
             "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def picture(name, sizes="100vw", cls="", loading="lazy", priority=False, alt=None):
    """<img> responsive in WebP con srcset, larghezza/altezza per evitare salti di layout."""
    img = current_app.config["IMAGES"].get(name)
    if not img:
        return ""
    files = img["files"]
    widths = sorted(int(w) for w in files)
    srcset = ", ".join(f"{url_for('static', filename='img/' + files[str(w)])} {w}w" for w in widths)
    default = files[str(widths[min(1, len(widths) - 1)])]
    alt_text = escape(alt if alt is not None else img["alt"])
    extra = ' fetchpriority="high"' if priority else ""
    load = "eager" if priority else loading
    return Markup(
        f'<img src="{url_for("static", filename="img/" + default)}" srcset="{srcset}" '
        f'sizes="{sizes}" width="{img["w"]}" height="{img["h"]}" alt="{alt_text}" '
        f'loading="{load}" decoding="async"{extra} class="{cls}">'
    )


def img_url(name, width=960):
    img = current_app.config["IMAGES"].get(name)
    if not img:
        return ""
    files = img["files"]
    w = str(width) if str(width) in files else sorted(files, key=int)[-1]
    return current_app.config["SITE_URL"] + url_for("static", filename="img/" + files[w])


def date_it(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {MONTHS_IT[d.month - 1]} {d.year}"


def address_line(loc):
    return f"{loc['street']}, {loc['postal_code']} {loc['city']} {loc['region']}"


def local_business_jsonld():
    """schema.org: un'organizzazione + un Florist per ogni chiosco, con @id distinti."""
    site = current_app.config["SITE_URL"]
    org_id = site + "/#organizzazione"
    graph = [{
        "@type": "Organization",
        "@id": org_id,
        "name": BUSINESS["name"],
        "alternateName": "La Rosa del Deserto – Fiorista Roma",
        "url": site + "/",
        "logo": site + url_for("static", filename="logo.svg"),
        "email": BUSINESS["email"],
        "telephone": BUSINESS["phone"],
        "founder": {"@type": "Person", "name": BUSINESS["owner"]},
        "sameAs": BUSINESS["same_as"],
        "description": "Fiorista a Roma con due chioschi di fiori e piante: Largo Ferdinando Gregorovius e Largo Santi Martiri dell'Uganda.",
    }]
    for loc in LOCATIONS:
        node = {
            "@type": "Florist",
            "@id": f"{site}/{loc['path']}/#chiosco",
            "name": loc["full_name"],
            "parentOrganization": {"@id": org_id},
            "url": f"{site}/{loc['path']}/",
            "telephone": loc["phone"],
            "image": img_url(loc["photo"]),
            "priceRange": "€€",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": loc["street"],
                "postalCode": loc["postal_code"],
                "addressLocality": loc["city"],
                "addressRegion": loc["region"],
                "addressCountry": "IT",
            },
            "geo": {"@type": "GeoCoordinates", "latitude": loc["lat"], "longitude": loc["lng"]},
            "hasMap": loc["maps_url"],
            "areaServed": [{"@type": "Place", "name": n + ", Roma"} for n in loc["nearby"]],
        }
        if loc["hours"]:
            node["openingHoursSpecification"] = [
                {"@type": "OpeningHoursSpecification", "dayOfWeek": d, "opens": o, "closes": c}
                for d, o, c in loc["hours"]
            ]
        graph.append(node)
    return {"@context": "https://schema.org", "@graph": graph}


def jsonld(data):
    return Markup('<script type="application/ld+json">' +
                  json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>")


def register(app):
    app.jinja_env.globals.update(
        picture=picture, img_url=img_url, BUSINESS=BUSINESS, LOCATIONS=LOCATIONS,
        SERVICES=SERVICES, NAV=NAV, address_line=address_line, jsonld=jsonld,
        local_business_jsonld=local_business_jsonld, DAYS_IT=DAYS_IT,
    )
    app.jinja_env.filters["date_it"] = date_it

    @app.context_processor
    def inject():
        return {
            "canonical": app.config["SITE_URL"] + request.path,
            "year": date.today().year,
            "phones_differ": len({l["phone"] for l in LOCATIONS}) > 1,
        }
