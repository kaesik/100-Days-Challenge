from flask import Flask, render_template
import requests as rq
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    name = rq.form["username"]
    password = rq.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)