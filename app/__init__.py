from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask
from app.blueprints.model import db
from app.blueprints.signup import signup
from app.blueprints.login import login
from app.blueprints.menu import menu
from app.blueprints.admin import admin


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "abcdefghijklmnop")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI","sqlite:///user.db")

    db.init_app(app)

    app.register_blueprint(signup)
    app.register_blueprint(login)
    app.register_blueprint(menu)
    app.register_blueprint(admin, url_prefix="/admin")

    with app.app_context():
        db.create_all()
    return app



