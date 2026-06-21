from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, jsonify, render_template,session,redirect, url_for
from app.blueprints.model import Movies, db

admin = Blueprint("admin", __name__)

@admin.route("/add-film", methods=["GET", "POST"])
def add_film():
    if request.method == "POST":
        title = request.form.get("title")
        duration = request.form.get("duration")
        origin = request.form.get("origin")
        date = request.form.get("date")
        age = request.form.get("age")
        genre = request.form.get("genre")
        img_url = request.form.get("img_url")

        if not title or not duration or not origin or not date or not age or not genre:
            return jsonify({"error": "Không được để trống thông tin bắt buộc"}), 400
        
        new_film = Movies(title=title, duration=duration, origin=origin, date=date, age=age, genre=genre, img_url=img_url)
        db.session.add(new_film)
        db.session.commit()

        return jsonify({"successfully": "Thêm phim thành công"}), 201

    if request.method == "GET":
        if not session.get('logged_in'):
            return redirect(url_for('login.login_user'))
        if session.get("role") != "admin":
            return "Bạn không phải là admin, không được phép thực hiện trong trang này"
        return render_template("add_film.html")


@admin.route("/delete-film", methods=["GET", "POST"])
def delete_film_with_id():
    if request.method == "POST":
        id = request.form.get("id_film")
        if not id:
            return jsonify({"error": "Phải nhập vào ID phim"}), 400
            
        found_id = Movies.query.get(id)
        if not found_id:
            return jsonify({"error": "Không tìm thấy bộ phim có ID này"}), 404
            
        db.session.delete(found_id)
        db.session.commit()
        return jsonify({"successfully": "Xóa phim thành công"}), 200
        
    if request.method == "GET":
        if not session.get('logged_in'):
            return redirect(url_for('login.login_user'))
        if session.get("role") != "admin":
            return "Bạn không phải là admin, không được phép thực hiện trong trang này"
        return render_template("add_film.html")