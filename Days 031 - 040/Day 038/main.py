import requests as rq

exercise = str(input("What exercise you did: "))

APP_ID =""
API_KEY = ""

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_param = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 180,
    "age": 26
}

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com"
NUTRITIONIX_ENDPOINT_EXERCISE = f"{NUTRITIONIX_ENDPOINT}/v2/natural/exercise"

response = rq.post(url=NUTRITIONIX_ENDPOINT_EXERCISE, data=exercise_param, headers=headers)

print(response.text)
