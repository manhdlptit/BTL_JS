from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, redirect, url_for, render_template
from app.blueprints.model import User, db

login = Blueprint("login", __name__)

@login.route("/login", methods = ["GET","POST"])
def login_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        find_username = User.query.filter(User.username == username).first()

        if not username or not password:
            return render_template("loi.html")
        if find_username is None:
            return render_template("loi.html")
        if password != find_username.password:
            return render_template("loi.html")

        return render_template("html.html")
    return render_template("login.html")


    
    

