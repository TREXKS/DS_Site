
import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    f = open("data/books.csv")
    reader = csv.reader(f)
    for isbn, title, author in reader:
        book = Books(startTime=startTime, currentTime=currentTime, daysPast=daysPast)
        db.session.add(book)
        print(f"Added book, {startTime} by {currentTime}, isbn {daysPast}.")
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
