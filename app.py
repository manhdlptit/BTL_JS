from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from app.blueprints.model import db
from app.blueprints.signup import signup
from app.blueprints.login import login
from app.blueprints.menu import menu
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "abcdefghijklmnop")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI","sqlite:///user.db")

db.init_app(app)

app.register_blueprint(signup)
app.register_blueprint(login)
app.register_blueprint(menu)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=2888)

