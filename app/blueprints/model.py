from dotenv import load_dotenv
load_dotenv()
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(31), nullable = False)
    email = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(17), nullable = False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
class Movies(db.Model):
    __tablename__ = "movies"
     
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    duration = db.Column(db.Integer, nullable = False)
    origin = db.Column(db.String(50), nullable = False) 
    date = db.Column(db.String(50), nullable = False) 
    age = db.Column(db.Integer, nullable = False) 
    genre = db.Column(db.String(50), nullable = False) 
    showtime = db.Column(db.String(50), nullable = False)
    img_url = db.Column(db.String(500), default = 'bg/id12.webp')

    def __init__(self, title, duration, origin, date, age, genre, showtime, img_url = None):
        self.title = title
        self.duration = duration
        self.origin = origin
        self.date = date
        self.age = age
        self.genre = genre
        self.showtime = showtime
        if img_url is not None:
            self.img_url = img_url
