from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, redirect, url_for, render_template, jsonify
from app.blueprints.model import User, db

menu = Blueprint("menu", __name__)

@menu.route("/homepage")
def homepage():
    return render_template("home.html")
@menu.route("/showtime")
def showtime():
    return render_template("calendar.html")
@menu.route("/intro")
def intro():
    return render_template("infor.html")
@menu.route("/shln")
def film_shln():
    return render_template("infor_film_shln.html")
