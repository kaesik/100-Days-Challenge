import requests as rq
from datetime import datetime

MY_LAT = 51.109872
MY_LNG = 17.032853

response = rq.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = {
    "lat": latitude,
    "lng": longitude
}

my_position = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
print(iss_position)

response2 = rq.get(url="https://api.sunrise-sunset.org/json", params=my_position)
response2.raise_for_status()
data2 = response2.json()

sunrise = data2["results"]["sunrise"]
sunset = data2["results"]["sunset"]

time_now = datetime.now()

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
print(time_now.hour)
