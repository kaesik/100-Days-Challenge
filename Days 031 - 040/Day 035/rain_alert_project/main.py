import requests as rq
from twilio.rest import Client

API_KEY = "key"
SID = "AC4840665656d8ca24abe7c133d4036e60"
TOKEN = "token"
MY_LAT = 51.099998
MY_LNG = 17.033331
CITY = "Wrocław,pl"


parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = rq.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]
will_rain = False


for hour_data in data_slice:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(SID, TOKEN)
    message = client.messages.create(
        body="Its goin to rain today. Bring Umbrella-ella-ella ☂",
        from_="+13613104234",
        to="my number"
    )
    print(message.status)

