from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config[""]

db = SQLAlchemy(app)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8888)

