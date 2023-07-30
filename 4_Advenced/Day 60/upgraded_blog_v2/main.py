from flask import Flask, render_template, request
import requests as rq
import smtplib as smtp
import ssl
app = Flask(__name__)

response = rq.get("https://api.npoint.io/51161e5bb72fb8a35b59").json()

MY_EMAIL = "kaes100day@gmail.com"
PASSWORD = "jxhztihhykavxxbz"
RECEIVER = "kamil.sobania.97@gmail.com"
context = ssl.create_default_context()

@app.route('/')
def main_page():
    return render_template("index.html", posts=response)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    is_true = False
    if request.method == 'POST':
        data = request.form
        print(data)
        is_true = True
        send_email(data)
        return render_template("contact.html", is_true=is_true)
    return render_template("contact.html", is_true=is_true)

@app.route('/blog/<num>')
def blog_page(num):
    post = response[int(num) - 1]
    return render_template("post.html", post=post)

def send_email(data):
    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    message = data["message"]
    with smtp.SMTP("smtp.gmail.com", port=587) as connection_gmail:
        connection_gmail.starttls()
        connection_gmail.login(user=MY_EMAIL, password=PASSWORD)
        connection_gmail.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER,
                                  msg=f"Subject:NEW MESSAGE\n\n"
                                      f"Name: {name}\n"
                                      f"E-mail: {email}\n"
                                      f"Telephone number: {phone}\n"
                                      f"Message: {message}")

if __name__ == "__main__":
    app.run(debug=True)