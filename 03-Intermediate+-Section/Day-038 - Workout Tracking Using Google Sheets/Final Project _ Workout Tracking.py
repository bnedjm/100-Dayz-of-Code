import os
import requests
from datetime import *

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "187"
AGE = "23"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com"

USER_ID = os.environ.get("USER_IDENTIFICATION")

TOKEN = os.environ.get("AUTH_TOKEN")

NUTRITIONIX_POST_ENDPOINT = f"{NUTRITIONIX_ENDPOINT}/v2/natural/exercise"
SHEETY_POST_ENDPOINT = f"https://api.sheety.co/{USER_ID}/myWorkouts/workouts"

Activity_txt = input("What exercises did you do?")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutritionix_params = {
 "query": Activity_txt,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE,
}

response = requests.post(url=NUTRITIONIX_POST_ENDPOINT, json=nutritionix_params, headers=nutritionix_headers)
response.raise_for_status()
data = response.json()["exercises"]

today = datetime.now()
day = today.strftime("%d/%m/%Y")
hour = today.strftime("%H:%M:%S")

sheety_headers = {
    "Authorization": TOKEN,
}

for activity in data:
    sheety_params = {
        "workout": {
            "date": day,
            "time": hour,
            "exercise": activity["name"].title(),
            "duration": int(activity["duration_min"]),
            "calories": int(activity["nf_calories"]),
        }
    }
    response = requests.post(url=SHEETY_POST_ENDPOINT, json=sheety_params, headers=sheety_headers)
    response.raise_for_status()
    print(response.text)
