from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, redirect, url_for, render_template
from app.blueprints.model import User, db

signup = Blueprint("signup", __name__)

@signup.route("/", methods = ["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        check_password = request.form.get("check_password")

        find_email = User.query.filter(User.email == email).first()
        find_username = User.query.filter(User.username == username).first()

        if not email or not username or not check_password or not password:
            return render_template("loi.html")
        if find_email is not None:
            return render_template("loi.html")
        if find_username is not None:
            return render_template("loi.html")
        if len(username) > 30:
            return render_template("loi.html")
        if len(password) > 16 or len(password)<8:
            return render_template("loi.html")
        if password != check_password:
            return render_template("loi.html")
    
        new_user = User(email=email,username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return render_template("html.html")
    return render_template("signup.html")


    
    

