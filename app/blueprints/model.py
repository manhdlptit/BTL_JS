from dotenv import load_dotenv
load_dotenv()
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id_user = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), nullable = False)
    email = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    role = db.Column(db.String(20), default = 'client')
    status = db.Column(db.String(20))

    def __init__(self, username, email, password, status, role = None):
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        if role is not None:
            self.role = role
    

class Movies(db.Model):
    __tablename__ = "movies"
     
    id_movie = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    duration = db.Column(db.Integer, nullable = False)
    origin = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(10000))
    date = db.Column(db.String(50), nullable = False) 
    age = db.Column(db.Integer, nullable = False) 
    genre = db.Column(db.String(50), nullable = False) 
    img_url = db.Column(db.String(500), default = 'bg/img/id12.webp')

    showtimes = db.relationship('Showtimes', backref='movie', lazy=True)

    def __init__(self, title, duration, origin, date, age, genre, description = None, img_url = None):
        self.title = title
        self.duration = duration
        self.origin = origin
        self.date = date
        self.age = age
        self.genre = genre
        if description is not None:
            self.description = description
        if img_url is not None:
            self.img_url = img_url


class Seats(db.Model):
    __tablename__ = "seats"

    id_seat = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.String(5), nullable=False)       
    number = db.Column(db.Integer, nullable=False)      
    seat_type = db.Column(db.String(20), default="STANDARD") 
    price_seat = db.Column(db.Integer)
    status = db.Column(db.String(20), default='AVAILABLE', nullable=False)

    def __init__(self, row, number, price_seat, status = None, seat_type = None):
        self.row = row
        self.number = number
        self.price_seat = price_seat
        if status is not None:
            self.status = status
        if seat_type is not None:
            self.seat_type = seat_type

    @property
    def name_seat(self):
        return f"{self.row}{self.number}"



class Showtimes(db.Model):
    __tablename__ = "showtimes"

    id_show_time = db.Column(db.Integer, primary_key=True)
    showtime = db.Column(db.String(7))
    id_movie = db.Column(db.Integer, db.ForeignKey('movies.id_movie'), nullable=False)

    def __init__(self, showtime, id_movie):
        self.showtime = showtime
        self.id_movie = id_movie




