import json
import os
from pathlib import Path

from flask import Flask

BASE = Path(__file__).resolve().parent


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-cambia-questa-chiave"),
        SITE_URL=os.environ.get("SITE_URL", "https://larosadeldesertodiseddrack.it").rstrip("/"),
        # Google tag (Ads/Analytics). Se vuoto, nessuno script di tracciamento e nessun banner cookie.
        GOOGLE_TAG_ID=os.environ.get("GOOGLE_TAG_ID", ""),
        # Etichetta conversione Google Ads per i clic su "Chiama" (es. AW-123/abcDEF).
        GOOGLE_ADS_CALL_CONVERSION=os.environ.get("GOOGLE_ADS_CALL_CONVERSION", ""),
        SEND_FILE_MAX_AGE_DEFAULT=60 * 60 * 24 * 30,
    )
    if test_config:
        app.config.update(test_config)

    with open(BASE / "data" / "images.json", encoding="utf-8") as f:
        app.config["IMAGES"] = json.load(f)
    with open(BASE / "data" / "posts.json", encoding="utf-8") as f:
        app.config["POSTS"] = json.load(f)

    from .routes import bp, legacy

    app.register_blueprint(bp)
    app.register_blueprint(legacy)

    from . import helpers

    helpers.register(app)

    return app
