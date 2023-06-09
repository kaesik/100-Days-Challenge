import os
import requests as rq


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.BEARER_AUTH = os.environ.get("BEARER_AUTH")
        self.SHEETY_API = os.environ.get("SHEETY_API")
        self.HEADERS = {
            "Content-Type": "application/json",
            "Authorization": self.BEARER_AUTH,
        }

    def get_data(self):
        sheety_get = rq.get(url=self.SHEETY_API, headers=self.HEADERS)
        sheety_get.raise_for_status()
        sheety_data = sheety_get.json()
        return sheety_data

    def put_iata_code(self, code, id):
        puts = {"price": {"iataCode": code}}
        sheety_put = rq.put(url=f"{self.SHEETY_API}/{id}", json=puts, headers=self.HEADERS)
        sheety_put.raise_for_status()

