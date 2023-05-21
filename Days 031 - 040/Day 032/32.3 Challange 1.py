import smtplib as smtp
import datetime as dt
import random as rd

# ----- MAILS ----- #
MY_EMAIL = "kaes100day@gmail.com"
PASSWORD = "jxhztihhykavxxbz"
SECOND_MAIL = "kamil.sobania.97@gmail.com"


# ----- TIMES ----- #
now = dt.datetime.now()
day_of_week = now.weekday()


# ----- QUOTE ----- #
def quote():
    with open("quotes.txt") as quotes:
        quotes_list = [quote for quote in quotes]
    random_quote = rd.choice(quotes_list)
    return random_quote


# ----- CODE ----- #
if day_of_week == 6:
    with smtp.SMTP("smtp.gmail.com") as connection_gmail:
        connection_gmail.starttls()
        connection_gmail.login(user=MY_EMAIL, password=PASSWORD)
        connection_gmail.sendmail(from_addr=MY_EMAIL, to_addrs=SECOND_MAIL,
                                  msg=f"Subject:Quote of the day\n\n"
                                      f"{quote()}")
