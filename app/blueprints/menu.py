from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, redirect, url_for, render_template, jsonify, session
from app.blueprints.model import Movies, Seats, db, Showtimes

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
    showtimes = Showtimes.query.all()
    movies = Movies.query.all()
    return render_template("showtime.html", movies = movies, showtimes = showtimes)
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
@menu.route("/seat", methods = ["GET", "POST"])
def seat():
    if request.method == "POST":
        data = request.form.get("list_seat_user_buy")
        # print("-----------------")
        # print("-----------------")
        # print(data)
        # print("-----------------")
        # print("-----------------")
        list_seat_user_buy_not_space = [
    
        ]
        list_fix = data.split(",")
        for seat in list_fix:
            row = seat[0]
            number = int(seat[1:])
            query_seat = Seats.query.filter_by(row=row, number=number).first()
            if query_seat:
                query_seat.status = "NOT_AVAILABLE"
            list_seat_user_buy_not_space.append(seat)
        db.session.commit()
        session["bought_seats"] = data
      
        return redirect(url_for("menu.invoice"))

    if request.method == "GET":
        if not session.get('logged_in'):
                return redirect(url_for('login.login_user'))
        seats = Seats.query.all()
        inf_user = {
            "username" : session.get("username"),
            "email": session.get('email')
        }
        return render_template("seat.html", seats = seats, inf_user =inf_user)

    
@menu.route("/invoice")
def invoice():
    if not session.get('logged_in'):
        return redirect(url_for('login.login_user'))
    bought_seats = session.get("bought_seats")
    
    inf_user = {
        "username": session.get("username"),
        "email": session.get('email')
    }
    
    return render_template("invoice.html", bought_seats=bought_seats, inf_user=inf_user)


@menu.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login.login_user'))
