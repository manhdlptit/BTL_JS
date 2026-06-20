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

    def __init__(self, username, email, password, status, role = None,):
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
    description = db.Column(db.String(1000))
    date = db.Column(db.String(50), nullable = False) 
    age = db.Column(db.Integer, nullable = False) 
    genre = db.Column(db.String(50), nullable = False) 
    img_url = db.Column(db.String(500), default = 'bg/id12.webp')

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


class MoviesCopyRight(db.Model):
    __tablename__ = "movie_copyright"

    id_movie_copyright = db.Column(db.Integer, primary_key = True)
    supplier = db.Column(db.String(100), nullable = False) 
    cost = db.Column(db.Float)
    expiry_date = db.Column(db.DateTime)
    id_movie = db.Column(db.Integer, db.ForeignKey('movies.id_movie'), nullable=False)


class Rooms(db.Model):
    __tablename__ = "rooms"

    id_room = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    seats = db.relationship('Seats', backref='room', lazy=True)
    showtimes = db.relationship('Showtimes', backref='room', lazy=True)

    def __init__(self, id_movie, supplier, cost=None, expiry_date=None):
        self.id_movie = id_movie
        self.supplier = supplier
        if cost is not None:
            self.cost = cost
        if expiry_date is not None:
            self.expiry_date = expiry_date


class Seats(db.Model):
    __tablename__ = "seats"

    id_seat = db.Column(db.Integer, primary_key=True)
    id_room = db.Column(db.Integer, db.ForeignKey('rooms.id_room'), nullable=False)
    row = db.Column(db.String(5), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    seat_type = db.Column(db.String(20), default="STANDARD")

    showtime_seats = db.relationship('ShowtimeSeat', backref='seat', lazy=True)

    def __init__(self, id_room, row, number, seat_type=None):
        self.id_room = id_room
        self.row = row
        self.number = number
        if seat_type is not None:
            self.seat_type = seat_type


class Showtimes(db.Model):
    __tablename__ = "showtimes"

    id_show_time = db.Column(db.Integer, primary_key=True)
    id_movie = db.Column(db.Integer, db.ForeignKey('movies.id_movie'), nullable=False)
    id_room = db.Column(db.Integer, db.ForeignKey('rooms.id_room'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False) 
    price = db.Column(db.Float, nullable=False)

    tickets = db.relationship('Tickets', backref='showtime', lazy=True)
    showtime_seats = db.relationship('ShowtimeSeat', backref='showtime', lazy=True)

    def __init__(self, id_movie, id_room, start_time, price):
        self.id_movie = id_movie
        self.id_room = id_room
        self.start_time = start_time
        self.price = price


class ShowtimeSeat(db.Model):
    __tablename__ = "showtime_seats"

    id_showtime_seat = db.Column(db.Integer, primary_key=True)
    id_show_time = db.Column(db.Integer, db.ForeignKey('showtimes.id_show_time'), nullable=False)
    id_seat = db.Column(db.Integer, db.ForeignKey('seats.id_seat'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=True) 
    status = db.Column(db.String(20), default='AVAILABLE', nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('id_show_time', 'id_seat', name='_showtime_seat_uc'),)

    def __init__(self, id_show_time, id_seat, id_user=None, status=None):
        self.id_show_time = id_show_time
        self.id_seat = id_seat
        if id_user is not None:
            self.id_user = id_user
        if status is not None:
            self.status = status


class Orders(db.Model):
    __tablename__ = "orders"

    id_orders = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)

    tickets = db.relationship('Tickets', backref='order', lazy=True)
    order_products = db.relationship('OrderProduct', backref='order', lazy=True)

    def __init__(self, id_user, total_amount, order_date=None):
        self.id_user = id_user
        self.total_amount = total_amount
        if order_date is not None:
            self.order_date = order_date


class Tickets(db.Model):
    __tablename__ = "tickets"

    id_ticket = db.Column(db.Integer, primary_key=True)
    id_orders = db.Column(db.Integer, db.ForeignKey('orders.id_orders'), nullable=False)
    id_show_time = db.Column(db.Integer, db.ForeignKey('showtimes.id_show_time'), nullable=False)
    seat_code = db.Column(db.String(10), nullable=False) 

    def __init__(self, id_orders, id_show_time, seat_code):
        self.id_orders = id_orders
        self.id_show_time = id_show_time
        self.seat_code = seat_code


class Products(db.Model):
    __tablename__ = "products"

    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

    order_products = db.relationship('OrderProduct', backref='product', lazy=True)

    def __init__(self, name, price, description=None):
        self.name = name
        self.price = price
        if description is not None:
            self.description = description


class OrderProduct(db.Model):
    __tablename__ = "order_product"

    id_order_product = db.Column(db.Integer, primary_key=True)
    id_orders = db.Column(db.Integer, db.ForeignKey('orders.id_orders'), nullable=False)
    id_product = db.Column(db.Integer, db.ForeignKey('products.id_product'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, id_orders, id_product, quantity=1):
        self.id_orders = id_orders
        self.id_product = id_product
        self.quantity = quantity