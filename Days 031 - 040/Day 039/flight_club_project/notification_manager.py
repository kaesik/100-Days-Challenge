import os
import requests as rq


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.TWILLIO_SID = os.environ.get("TWILLIO_SID")
        self.TWILLIO_TOKEN = os.environ.get("TWILLIO_TOKEN")

    def create_msg(self, data):
        from_iata = data["from_iata"]
        from_city = data["from_city"]
        to_iata = data["to_iata"]
        to_city = data["to_city"]
        ticket_price = data["ticket_price"]
        dep_time = data["dep_time"]
        dep_date = data["dep_date"]
        arr_time = data["arr_time"]
        arr_date = data["arr_date"]
        message = f"There was a cheap ticket.\n" \
                  f"Departure from {from_city}, {from_iata} on {dep_date} at {dep_time} to {to_city}, {to_iata}.\n" \
                  f"Estimated arrival date is {arr_date} at {arr_time}. The ticket costs {ticket_price}€."
        return message


