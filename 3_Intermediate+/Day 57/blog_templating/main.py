from flask import Flask, render_template
import requests as rq


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = rq.get(blog_url).json()
    return render_template("index.html", posts=response)

@app.route('/post/<num>')
def get_post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = rq.get(blog_url).json()
    return render_template("post.html", post=response[int(num)-1])

if __name__ == "__main__":
    app.run(debug=True)
