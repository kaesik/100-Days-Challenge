from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

data_man = DataManager()
data_fli = FlightData()
noti_man = NotificationManager()


def upload_iata():
    for i in range(0, len(data_man.get_data()["prices"])):
        city = data_man.get_data()["prices"][i]["city"]
        id = data_man.get_data()["prices"][i]["id"]
        code = data_fli.get_iata(city)
        print(city, id, code)
        data_man.put_iata_code(code, id)


def get_flights(iata):
    for a in range(0, len(data_man.get_data()["prices"])):
        actual_iata = data_man.get_data()["prices"][a]["iataCode"]
        price = int(data_man.get_data()["prices"][a]["lowestPrice"])
        if actual_iata == iata:
            try:
                flight_data = data_fli.get_flight_data(iata, price)
                for b in range(0, len(data_man.get_users_data()["users"])):
                    first = data_man.get_users_data()["users"][b]["firstName"]
                    last = data_man.get_users_data()["users"][b]["lastName"]
                    email = data_man.get_users_data()["users"][b]["email"]
                    message = noti_man.create_msg(flight_data, first, last)
                    noti_man.send_email(message, email)
            except IndexError:
                print(f"There is not ticket for {actual_iata}.")


register = input("Do you want register? y/n\n").lower()
if register == "y":
    data_man.register()
else:
    pass

for c in range(0, len(data_man.get_data()["prices"])):
    iata = data_man.get_data()["prices"][c]["iataCode"]
    get_flights(iata)


# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

# Program Requirements
# 1 Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International
# Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports,
# you want the city code (not the airport code see here).✅
#
# 2 Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in
# the Google Sheet.✅
#
# 3 If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with
# the Twilio API.✅
#
# 4 The SMS should include the departure airport IATA code, destination airport IATA code, departure city,
# destination city, flight price and flight dates. e.g.✅
