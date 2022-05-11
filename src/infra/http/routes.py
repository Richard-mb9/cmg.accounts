from flask import Flask
from src.infra.http.users_info.api import app as users_info_app
from src.infra.http.adresses.api import app as adresses_app
from src.infra.http.telephones.api import app as telephones_app
from src.infra.http.telephones.api import app as stores_app


def create_routes(app: Flask):
    app.register_blueprint(users_info_app, url_prefix='/users-info')
    app.register_blueprint(adresses_app, url_prefix='/adresses')
    app.register_blueprint(telephones_app, url_prefix='/telephones')
    app.register_blueprint(stores_app, url_prefix='/stores')