# ----- Extra Hard Starting Project ----- #
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib as smtp
import pandas as pd
import random as rd


# ----- CONSTANTS ---- #
EMAIL = "kaes100day@gmail.com"
PASSWORD = "jxhztihhykavxxbz"


# ----- FUNCTIONS ----- #
def make_letter(name):
    num = rd.randint(1, 3)
    with open(f"./letter_templates/letter_{num}.txt") as letter:
        text = letter.read()
        text = text.replace("[NAME]", name)
    return text


def send_mail(letter, user, password, addressee):
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr=user, to_addrs=addressee,
                                  msg=f"Subject:Happy Birthday!\n\n"
                                      f"{letter}")


def check_date(checked_month, checked_day):
    now = dt.datetime.now()
    month = now.month
    day = now.day
    if month == checked_month and day == checked_day:
        return True
    else:
        return False


def get_info(index):
    data = pd.read_csv("./birthdays.csv")
    name = data["name"][index]
    email = data["email"][index]
    month = data["month"][index]
    day = data["day"][index]
    return name, email, month, day


# ----- CODE ----- #
file = pd.read_csv("./birthdays.csv")

for i in file.index:
    name, email, month, day = get_info(i)
    letter = make_letter(name)

    if check_date(month, day):
        send_mail(letter, EMAIL, PASSWORD, email)




