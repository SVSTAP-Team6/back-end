import os
from importlib import import_module
from importlib.util import find_spec as importlib_find
from flask_cors import CORS
from flask import Flask
from flask_migrate import Migrate

from grain.blueprints import all_blueprints
from grain.libs.database import db


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    phase = os.getenv('GRAIN_ENV', 'dev/').lower()
    app.config.from_pyfile('../config/%s/config.cfg' % phase)

    # CORS
    cors = CORS(app, resources={r"/*": {
        "origins": "['http://localhost:3000']",
        "allow_headers": "*",
        "expose_headers": "*"}}, supports_credentials=True)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprint
    for bp in all_blueprints:
        path_name = importlib_find(bp.import_name)
        import_module(path_name.name)
        app.register_blueprint(bp, url_prefix=bp.url_prefix)

    return app
