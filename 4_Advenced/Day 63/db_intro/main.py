from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # create the extension
app = Flask(__name__) # create the app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db" # configure the SQLite database, relative to the app instance folder
db.init_app(app) # initialize the app with the extension

class Book(db.Model): # CREATE TABLE
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rate = db.Column(db.Float, nullable=False)

    def __repr__(self): # Optional: this will allow each book object to be identified by its title when printed.
        return f'<Book {self.title}>'

with app.app_context(): # Create table schema in the database. Requires application context.
    db.create_all()

with app.app_context(): # CREATE RECORD
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rate=9.3)
    db.session.add(new_book)
    db.session.commit()
