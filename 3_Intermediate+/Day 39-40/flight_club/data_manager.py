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
        sheety_get = rq.get(url=f"{self.SHEETY_API}/prices", headers=self.HEADERS)
        sheety_get.raise_for_status()
        sheety_data = sheety_get.json()
        return sheety_data

    def get_users_data(self):
        sheety_get = rq.get(url=f"{self.SHEETY_API}/users", headers=self.HEADERS)
        sheety_get.raise_for_status()
        sheety_data = sheety_get.json()
        return sheety_data

    def put_iata_code(self, code, id):
        puts = {"price": {"iataCode": code}}
        sheety_put = rq.put(url=f"{self.SHEETY_API}/prices/{id}", json=puts, headers=self.HEADERS)
        sheety_put.raise_for_status()

    def check_mail(self):
        email = input("What is your email?\n")
        check = input("Type your email again.\n")
        if email == check:
            return email
        else:
            print("Something is wrong, write again.")
            self.check_mail()

    def reg_name(self, id):
        first = "Kamil"
        puts = {"users": {"firstName": first}}
        sheety_add = rq.post(url=f"{self.SHEETY_API}/users", headers=self.HEADERS)
        sheety_add.raise_for_status()
        sheety_put = rq.put(url=f"{self.SHEETY_API}/users/{id}", json=puts, headers=self.HEADERS)
        sheety_put.raise_for_status()

    def register(self):
        first = input("What is your first name?\n")
        last = input("What is your last name?\n")
        email = self.check_mail()
        puts = {
            "user": {
                "firstName": first,
                 "lastName": last,
                 "email": email
             }
        }
        sheety_put = rq.post(url=f"{self.SHEETY_API}/users", json=puts, headers=self.HEADERS)
        sheety_put.raise_for_status()

