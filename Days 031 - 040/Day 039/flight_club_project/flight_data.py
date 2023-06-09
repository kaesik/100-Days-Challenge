import os
import requests as rq
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd


class FlightData:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self):
        self.TODAY = dt.now().strftime("%d/%m/%Y")
        self.FUTURE = (dt.now() + rd(months=+6)).strftime("%d/%m/%Y")
        self.TEQUILLA_API = "https://api.tequila.kiwi.com/"
        self.API_KEY = os.environ.get("TEQUILLA_API_KEY")
        self.HEADERS = {"apikey": self.API_KEY}

    def get_iata(self, city):
        iata_params = {"term": city, "location_types": "city"}
        iata_get = rq.get(url=f"{self.TEQUILLA_API}locations/query/", params=iata_params, headers=self.HEADERS)
        iata_get.raise_for_status()
        iata_data = iata_get.json()["locations"]
        code = iata_data[0]["code"]
        return code

    def get_flight_data(self, to_code, max_price):
        params = {
            "fly_from": "WRO",
            "fly_to": to_code,
            "date_from": self.TODAY,
            "date_to": self.FUTURE,
            "price_to": max_price,
            "vehicle_type": "aircraft",
            "sort": "price"
        }
        flight_get = rq.get(url=f"{self.TEQUILLA_API}v2/search/", params=params, headers=self.HEADERS)
        flight_get.raise_for_status()
        flight_data = flight_get.json()["data"]
        flight_data = {
            "from_iata": flight_data[0]["flyFrom"],
            "from_city": flight_data[0]["cityFrom"],
            "to_iata": flight_data[0]["flyTo"],
            "to_city": flight_data[0]["cityTo"],
            "ticket_price": flight_data[0]["price"],
            "dep_time": flight_data[0]["utc_departure"][11:16],
            "dep_date": flight_data[0]["utc_departure"][:10],
            "arr_time": flight_data[0]["utc_arrival"][11:16],
            "arr_date": flight_data[0]["utc_arrival"][:10],
        }
        return flight_data





# 4 The SMS should include the departure airport IATA code, destination airport IATA code, departure city,
# destination city, flight price and flight dates. e.g.
