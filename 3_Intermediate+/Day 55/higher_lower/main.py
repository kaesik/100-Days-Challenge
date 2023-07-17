from flask import Flask
import random as rd
app = Flask(__name__)

RD_NUMBER = rd.randint(0, 9)
RD_NUMBER = 3
HOME_GIF = "https://64.media.tumblr.com/78e2633d4e5b5d6a487dc0eb088e023d/tumblr_noha2qkitT1rb40pco1_500.gifv"
HIGH_GIF = "https://media1.giphy.com/media/l2YWy9pD8sZEUMF0s/giphy.gif?cid=ecf05e479fw40mu0cd1esc8vsbduwlo4ls6f7fffid44bpd0&ep=v1_gifs_search&rid=giphy.gif&ct=g"
LOW_GIF = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGp4czlwNWh5NWRncnhlcms1YmhzZ3dvbndkdm41c3Rkam5idzJmMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif"
FOUND_GIF = "https://media1.giphy.com/media/2m1lj8p8v6JcWpREtL/giphy.gif?cid=ecf05e47gmm4j5vrou4bpgmnmgc062pzfaru6jjckd62yfpv&ep=v1_gifs_search&rid=giphy.gif&ct=g"

@app.route('/')
def home_site():
    title = "Guess a number between 0 and 9"
    return f'<h1>{title}</h1>\n' \
           f'<img src="{HOME_GIF}">'

@app.route('/<number>')
def number_site(number):
    if int(number) > RD_NUMBER:
        title = "Too high, try again!"
        gif = HIGH_GIF
    elif int(number) < RD_NUMBER:
        title = "Too low, try again!"
        gif = LOW_GIF
    else:
        title = "You found me!"
        gif = FOUND_GIF
    return f'<h1>{title}</h1>\n' \
             f'<img src="{gif}">'


if __name__ == "__main__":
    app.run(debug=True)