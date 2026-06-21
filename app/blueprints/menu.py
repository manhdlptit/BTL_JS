from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, redirect, url_for, render_template, jsonify, session
from app.blueprints.model import Movies, Seats

menu = Blueprint("menu", __name__)

@menu.route("/homepage")
def homepage():
    if not session.get('logged_in'):
            return redirect(url_for('login.login_user'))
    return render_template("home.html")
@menu.route("/showtime")
def showtime():
    if not session.get('logged_in'):
            return redirect(url_for('login.login_user'))
    movies = Movies.query.all()
    return render_template("showtime.html", movies = movies)
@menu.route("/intro")
def intro():
    if not session.get('logged_in'):
            return redirect(url_for('login.login_user'))
    return render_template("infor.html")
@menu.route("/shln")
def film_shln():
    if not session.get('logged_in'):
            return redirect(url_for('login.login_user'))
    return render_template("infor_film_shln.html")
@menu.route("/shop-item")
def shop_item():
    if not session.get('logged_in'):
            return redirect(url_for('login.login_user'))
    return render_template("shop.html")
@menu.route("/checkout-item")
def checkout_item():
    if not session.get('logged_in'):
            return redirect(url_for('login.login_user'))
    return render_template("checkou.html")
@menu.route("/seat")
def seat():
    if not session.get('logged_in'):
            return redirect(url_for('login.login_user'))
    seats = Seats.query.all()
    inf_user = {
        "username" : session.get("username"),
        "email": session.get('email')
    }
    return render_template("seat.html", seats = seats, inf_user = inf_user)

@menu.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login.login_user'))