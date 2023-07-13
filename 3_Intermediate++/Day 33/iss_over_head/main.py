import requests as rq
from datetime import datetime
import smtplib as smtp
import time

MY_LAT = 51.109872
MY_LNG = 17.032853
MY_EMAIL = "kaes100day@gmail.com"
PASSWORD = "jxhztihhykavxxbz"
RECEIVER = "kamil.sobania.97@gmail.com"

response = rq.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = rq.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    # If the ISS is close to my current position,
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        if MY_LNG-5 <= iss_longitude <= MY_LNG+5:
            check_iss = True
        else:
            check_iss = False
    else:
        check_iss = False

    # and it is currently dark
    if sunrise <= time_now.hour <= sunset:
        check_time = True
    else:
        check_time = False
    # Then email me to tell me to look up.
    if check_iss and check_time:
        with smtp.SMTP("smtp.gmail.com") as connection_gmail:
            connection_gmail.starttls()
            connection_gmail.login(user=MY_EMAIL, password=PASSWORD)
            connection_gmail.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER,
                                      msg="Subject:ISS IS HERE\n\n"
                                          "Look up! There might be ISS.")
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
