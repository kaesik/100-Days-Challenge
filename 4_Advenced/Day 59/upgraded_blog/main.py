from flask import Flask, render_template
import requests as rq
app = Flask(__name__)

blog_url = "https://api.npoint.io/51161e5bb72fb8a35b59"
response = rq.get(blog_url).json()

@app.route('/')
def main_page():
    return render_template("index.html", posts=response)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/blog/<num>')
def blog_page(num):
    post = response[int(num) - 1]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)