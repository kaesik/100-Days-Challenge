from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///virtual_bookshelf.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()
        return render_template("index.html", books=all_books)
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(
                title=request.form["title"],
                author=request.form["author"],
                rating=request.form["rating"].replace(",", ".")
            )
            print(new_book)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"].replace(",", ".")
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"].replace(",", ".")
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
