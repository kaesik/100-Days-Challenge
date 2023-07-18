from flask import Flask, render_template
import random as rd
import datetime as dt
import requests as rq

app = Flask(__name__)

@app.route('/')
def hello():
    random_number = rd.randint(1, 10)
    current_year = dt.datetime.now().year
    return render_template("index.html", num=random_number, cur_yr=current_year)

@app.route('/guess/<name>')
def guess(name):
    name = name.capitalize()
    age = rq.get(url=f"https://api.agify.io/?name={name}").json()["age"]
    gender = rq.get(url=f"https://api.genderize.io/?name={name}").json()["gender"]
    return render_template("index.html", name=name, age=age, gender=gender)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = rq.get(blog_url).json()
    return render_template("blog.html", posts=response)

if __name__ == "__main__":
    app.run(debug=True)
