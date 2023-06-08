import os
import requests as rq
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rd


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self):
        self.TODAY = dt.now().strftime("%d/%m/%Y")
        self.FUTURE = (dt.now() + rd(months=+6)).strftime("%d/%m/%Y")
        self.TEQUILLA_API = "https://api.tequila.kiwi.com/"
        self.API_KEY = os.environ.get("TEQUILLA_API_KEY")
        self.HEADERS = {"apikey": self.API_KEY}

    def get_flights(self, from_code, to_code):
        params = {
            "fly_from": from_code,
            "fly_to": to_code,
            "date_from": self.TODAY,
            "date_to": self.FUTURE,
        }
        flight_get = rq.get(url=f"{self.TEQUILLA_API}v2/search/", params=params, headers=self.HEADERS)
        flight_get.raise_for_status()
        flight_data = flight_get.json()
        return flight_data

    def get_iata(self, city):
        iata_params = {"term": city, "location_types": "city"}
        iata_get = rq.get(url=f"{self.TEQUILLA_API}locations/query/", params=iata_params, headers=self.HEADERS)
        iata_get.raise_for_status()
        iata_data = iata_get.json()["locations"]
        code = iata_data[0]["code"]
        return code

    pass
