# terminal:
#   set FLASK_APP=hello.py
#   $env:FLASK_APP = "C:\Users\kamil\PycharmProjects\100_Days_of_Code\3_Intermediate+\Day 54\flask\hello.py"
#   higher_lower run

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'Bye!'

if __name__ == "__main__":
    app.run()