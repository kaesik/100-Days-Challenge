from flask import Flask
app = Flask(__name__)



@app.route('/')
def home_site():
    gif = "https://64.media.tumblr.com/78e2633d4e5b5d6a487dc0eb088e023d/tumblr_noha2qkitT1rb40pco1_500.gifv"
    title = "Guess a number between 0 and 9"
    return f'<h1>{title}</h1>\n' \
           f'<img src="{gif}">'

@app.route('/<number>')
def number_site(number):


if __name__ == "__main__":
    app.run(debug=True)