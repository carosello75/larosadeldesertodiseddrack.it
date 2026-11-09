from flask import Blueprint, Response, abort, current_app, redirect, render_template, url_for

from .site_data import BUSINESS, LOCATIONS, SERVICES

bp = Blueprint("main", __name__)
legacy = Blueprint("legacy", __name__)

LOC_BY_PATH = {l["path"]: l for l in LOCATIONS}
LOC_BY_SLUG = {l["slug"]: l for l in LOCATIONS}
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}


def images_in(cat):
    return [k for k, v in current_app.config["IMAGES"].items() if v["cat"] == cat]


@bp.route("/")
def home():
    posts = current_app.config["POSTS"][:3]
    strip = ["cuore-di-rose-rosse", "bouquet-sposa-rose-avorio", "corona-alloro-laurea",
             "girasoli", "centrotavola-natale-mele", "bouquet-tulipani-rosa",
             "corona-funebre-gerbere", "rose-blu-bouquet"]
    return render_template("home.html", posts=posts, strip=strip)


@bp.route("/servizi/")
def services():
    return render_template("services.html")


@bp.route("/servizi/<slug>/")
def service(slug):
    s = SERVICE_BY_SLUG.get(slug) or abort(404)
    gallery = [n for n in s.get("extra", []) + images_in(s["cat"]) if n != s["cover"]][:9]
    others = [x for x in SERVICES if x["slug"] != slug][:4]
    return render_template("service.html", s=s, gallery=gallery, others=others)


@bp.route("/<any(%s):path>/" % ",".join(repr(p) for p in LOC_BY_PATH))
def location(path):
    loc = LOC_BY_PATH[path]
    other = next(l for l in LOCATIONS if l is not loc)
    posts = [p for p in current_app.config["POSTS"]
             if (loc["slug"] == "uganda" and ("uganda" in p["slug"] or "laurentina" in p["slug"] or "montagnola" in p["slug"]))
             or (loc["slug"] == "gregorovius" and ("gregorovius" in p["slug"] or "macedonia" in p["slug"]))]
    return render_template("location.html", loc=loc, other=other, posts=posts)


@bp.route("/galleria/")
def gallery():
    cats = [("sposa", "Bouquet da sposa"), ("matrimoni", "Matrimoni e cerimonie"),
            ("bouquet", "Bouquet e composizioni"), ("sanvalentino", "San Valentino"),
            ("regali", "Regali: dolci, peluche e palloncini"),
            ("autunno", "Autunno"), ("natale", "Natale"), ("laurea", "Lauree"),
            ("funerali", "Cordoglio e funerali"), ("piante", "Piante"),
            ("youssef", "Youssef al lavoro"), ("hero", "I chioschi")]
    groups = [(label, cat, images_in(cat)) for cat, label in cats]
    return render_template("gallery.html", groups=groups)


@bp.route("/dove-siamo/")
def where():
    return render_template("where.html")


@bp.route("/blog/")
def blog():
    return render_template("blog.html", posts=current_app.config["POSTS"])


@bp.route("/blog/<slug>/")
def post(slug):
    posts = current_app.config["POSTS"]
    p = next((x for x in posts if x["slug"] == slug), None) or abort(404)
    more = [x for x in posts if x["slug"] != slug][:3]
    return render_template("post.html", p=p, more=more)


@bp.route("/prenota/")
def booking():
    return render_template("booking.html")


@bp.route("/manifest.webmanifest")
def manifest():
    return current_app.response_class(render_template("manifest.webmanifest"),
                                      mimetype="application/manifest+json")


@bp.route("/sw.js")
def service_worker():
    return current_app.response_class(render_template("sw.js"), mimetype="text/javascript")


@bp.route("/offline/")
def offline():
    return render_template("offline.html")


@bp.route("/preventivo/")
def quote_request():
    return render_template("quote.html", kind="preventivo")


@bp.route("/contatti/")
def contacts():
    return render_template("contacts.html", kind="contatti")


@bp.route("/pagamento/")
def payment():
    return render_template("payment.html")


@bp.route("/cookie-policy/")
def cookies():
    return render_template("cookies.html")


@bp.route("/privacy/")
def privacy():
    return render_template("privacy.html")


@bp.route("/robots.txt")
def robots():
    site = current_app.config["SITE_URL"]
    return Response(f"User-agent: *\nAllow: /\n\nSitemap: {site}/sitemap.xml\n", mimetype="text/plain")


@bp.route("/sitemap.xml")
def sitemap():
    site = current_app.config["SITE_URL"]
    urls = [url_for("main.home"), url_for("main.booking"), url_for("main.services"), url_for("main.gallery"),
            url_for("main.where"), url_for("main.blog"), url_for("main.quote_request"),
            url_for("main.contacts"), url_for("main.payment")]
    urls += [f"/{l['path']}/" for l in LOCATIONS]
    urls += [url_for("main.service", slug=s["slug"]) for s in SERVICES]
    urls += [url_for("main.post", slug=p["slug"]) for p in current_app.config["POSTS"]]
    body = "".join(f"<url><loc>{site}{u}</loc></url>" for u in urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>')
    return Response(xml, mimetype="application/xml")


@bp.app_errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


# ---- Redirect permanenti dai vecchi indirizzi WordPress (conservano il posizionamento) ----
OLD_PAGES = {
    "piante-e-fiori-roma": "main.home",
    "la-nostra-gallery": "main.gallery",
    "shop": "main.payment",
    "cookie-policy-ue": "main.cookies",
}
OLD_CATEGORIES = {
    "largo-santi-martiri-delluganda-roma": "/fioraio-largo-santi-martiri-uganda/",
    "fiorista-l-ferdinando-gregorovius": "/fioraio-largo-ferdinando-gregorovius/",
    "addobbi-matrimoniali": "/servizi/addobbi-matrimoni/",
    "addobbi-floreali-eur-laurentina": "/servizi/addobbi-matrimoni/",
    "terrazze-e-giardini": "/servizi/piante-terrazze-e-giardini/",
}


@legacy.route("/<any(%s):old>/" % ",".join(repr(p) for p in OLD_PAGES))
def old_page(old):
    return redirect(url_for(OLD_PAGES[old]), 301)


@legacy.route("/per-natale/")
def old_natale():
    return redirect(url_for("main.post", slug="per-natale"), 301)


@legacy.route("/<int:y>/<int:m>/<int:d>/<slug>/")
def old_post(y, m, d, slug):
    return redirect(url_for("main.post", slug=slug), 301)


@legacy.route("/category/<slug>/")
def old_category(slug):
    return redirect(OLD_CATEGORIES.get(slug, url_for("main.blog")), 301)


@legacy.route("/feed/")
def old_feed():
    return redirect(url_for("main.blog"), 301)
