from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, redirect, url_for, render_template, jsonify
from app.blueprints.model import User, db
from app.blueprints.login import login

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
            return jsonify({"error": "not null any value"}),400  
        if find_email is not None:
            return jsonify({"error": "email existed"}),400      
        if find_username is not None:
            return jsonify({"error": "username existed"}),400      
        if len(username) > 30:
            return jsonify({"error": "length username must shorter than 30 character"}),400         
        if len(password) > 16 or len(password)<8:
            return jsonify({"error": "8 <= length password <= 16"}),400      
        if password != check_password:
            return jsonify({"error": "password different check password"}),400     
    
        new_user = User(email=email,username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login.login_user"))
    return render_template("signup.html")


    
    

