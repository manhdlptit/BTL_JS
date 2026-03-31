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
    
