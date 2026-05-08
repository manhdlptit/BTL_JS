from dotenv import load_dotenv
load_dotenv()
from flask import Blueprint, request, jsonify, render_template
from app.blueprints.model import Movies, db

admin = Blueprint("add_film", __name__)

@admin.route("/add-film", methods = ["GET", "POST"])
def addFilm():
    if request.method == "POST":
        title = request.form.get("title")
        duration = request.form.get("duration")
        origin = request.form.get("origin")
        date = request.form.get("date")
        age = request.form.get("age")
        genre = request.form.get("genre")
        showtime = request.form.get("showtime")
        img_url = request.form.get("img_url")

        if not title or not duration or not origin or not date or not age or not genre or not showtime:
            return jsonify({"error": "not null any value"}), 400
        
        new_film = Movies(title=title, duration=duration, origin=origin, date=date, age=age, genre=genre, showtime=showtime, img_url=img_url)
        db.session.add(new_film)
        db.session.commit()

        return jsonify({"sucessfully" : "them phim thanh cong"}), 201

    return render_template("add_film.html")


@admin.route("/delete-film", methods = ["GET", "POST"])
def delete_film_with_id():
    if request.method == "POST":
        id = request.form.get("id_film")
        if not id:
            return jsonify({"error": "Phai nhap vao id"}), 400
        found_id = Movies.query.get(id)
        if not found_id:
            return jsonify({"error": "Khong thay film"}), 400
        db.session.delete(found_id)
        db.session.commit()
        return jsonify({"sucessfully" : "xoa phim thanh cong"}), 201
    return render_template("delete_film.html")