from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, redirect, url_for, render_template, jsonify
from app.blueprints.model import User, db
from app.blueprints.menu import menu

login = Blueprint("login", __name__)

@login.route("/login", methods = ["GET","POST"])
def login_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        find_username = User.query.filter(User.username == username).first()

        if not username or not password:
            return jsonify({"error": "not null any value"}),400    
        if find_username is None:
            return jsonify({"error": "not find username"}),404   
        if password != find_username.password:
            return jsonify({"error": "password different check password"}),400    

        return redirect(url_for("menu.homepage"))
    if request.method == "GET":
        return render_template("login.html")


    
    

