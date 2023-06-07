import requests as rq
from requests.auth import HTTPBasicAuth
import os
from datetime import datetime

exercise_input = str(input("What exercise you did: "))
# exercise_input = "run 5km"
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
BASIC_AUTH = os.environ.get("BASIC_AUTH")
BEARER_AUTH = os.environ.get("BEARER_AUTH")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
auth_headers = {
    "Content-Type": "application/json",
    "Authorization": BASIC_AUTH,
}
exercise_param = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 180,
    "age": 26
}

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com"
NUTRITIONIX_ENDPOINT_EXERCISE = f"{NUTRITIONIX_ENDPOINT}/v2/natural/exercise"
SHEETY_ROWS = "https://api.sheety.co/55148d049aa169cc18fb8e797d0e08ff/workoutTracking/workouts"

exercises = rq.post(url=NUTRITIONIX_ENDPOINT_EXERCISE, data=exercise_param, headers=headers)
exercises.raise_for_status()
exercise_data = exercises.json()

for exercise_data in exercise_data["exercises"]:
    exercise = exercise_data["user_input"].title()
    duration = exercise_data["duration_min"]
    calories = exercise_data["nf_calories"]
    post = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
    }}
    sheety = rq.post(
        url=SHEETY_ROWS,
        json=post,
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        headers=auth_headers,
    )

