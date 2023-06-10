import os
import requests as rq
import smtplib as smtp
from twilio.rest import Client


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.TWILLIO_SID = os.environ.get("TWILLIO_SID")
        self.TWILLIO_TOKEN = os.environ.get("TWILLIO_TOKEN")
        self.USER = "kaes100day@gmail.com"
        self.PASSWORD = os.environ.get("PASSWORD")

    def create_msg(self, data, name, lastname):
        from_iata = data["from_iata"]
        from_city = data["from_city"]
        to_iata = data["to_iata"]
        to_city = data["to_city"]
        ticket_price = data["ticket_price"]
        dep_time = data["dep_time"]
        dep_date = data["dep_date"]
        arr_time = data["arr_time"]
        arr_date = data["arr_date"]
        message = f"Hello {name} {lastname}!\n" \
                  f"Departure from {from_city}, {from_iata} on {dep_date} at {dep_time} to {to_city}, {to_iata}.\n" \
                  f"Estimated arrival date is {arr_date} at {arr_time}. The ticket costs {ticket_price}€."
        return message

    def send_msg(self, sms):
        client = Client(self.TWILLIO_SID, self.TWILLIO_TOKEN)
        message = client.messages.create(
            body=sms,
            from_="+13613104234",
            to="+48695225397"
        )

    def send_email(self, message, adrs):
        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.USER, password=self.PASSWORD)
            connection.sendmail(from_addr=self.USER, to_addrs=adrs,
                                msg=f"Subject:Cheap tickets!\n\n"
                                    f"{message}".encode('utf-8'))
