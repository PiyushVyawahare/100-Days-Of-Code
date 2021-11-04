from datetime import datetime

import requests

APP_ID = "29766b2e"
API_KEY = "6cfadd8277f0e6fa01ae9f4c2050b61d"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/85dfd0b36a48432768503f2dba67fc15/workoutTracking/workouts"

exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 73.0,
    "height_cm": 170.58,
    "age": 20
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()

# ---------------------- Start of Step 4 Solution ---------------------- #

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
	