from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, redirect, url_for, render_template, jsonify
from app.blueprints.model import Movies

menu = Blueprint("menu", __name__)

@menu.route("/homepage")
def homepage():
    return render_template("home.html")
@menu.route("/showtime")
def showtime():
    movies = Movies.query.all()
    return render_template("showtime.html", movies = movies)
@menu.route("/intro")
def intro():
    return render_template("infor.html")
@menu.route("/shln")
def film_shln():
    return render_template("infor_film_shln.html")
@menu.route("/abc")
def abc():
    movies = Movies.query.all()
    return render_template("abc.html", movies = movies)
