from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db.init_app(app)

headers = {
            "accept": "application/json",
            "Authorization": os.environ.get("MOVIE_DB_API_KEY")
        }


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

class EditMovieForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5')
    review = StringField('Your Review')
    submit = SubmitField('Submit')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    for movie in all_movies:
        movie.ranking = len(all_movies) - all_movies.index(movie)
        db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/", methods=["GET", "POST"])
def edit():
    form = EditMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if request.method == "POST":
        movie_rating = request.form["rating"]
        if movie_rating:
            movie.rating = float(form.rating.data.replace(",", "."))
        else:
            pass

        movie_review = request.form["review"]
        if movie_review:
            movie.review = form.review.data
        else:
            pass

        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete/")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add/", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if request.method == "POST":
        movie_title = request.form["title"]
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        movies = response.json()["results"]
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)

@app.route("/select/")
def select():
    movie_id = request.args.get("id")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    movie = response.json()
    new_movie = Movie(
        title=movie["title"],
        year=movie["release_date"].split("-")[0],
        description=movie["overview"],
        rating=0,
        ranking=0,
        review="",
        img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
