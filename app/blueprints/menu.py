from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, redirect, url_for, render_template, jsonify
from app.blueprints.model import User, db

menu = Blueprint("menu", __name__)

@menu.route("/homepage")
def homepage():
    return render_template("html.html")
@menu.route("/showtime")
def showtime():
    return render_template("html.html")
@menu.route("/intro")
def intro():
    return render_template("intro.html")
