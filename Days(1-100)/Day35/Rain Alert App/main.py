import requests
from twilio.rest import Client

API_KEY = "4de616e82a48a55bea795b6852f39a58"

account_sid = "AC77e9d87ccf45ef690cdf729ac3a6d1d0"
auth_token = "c66287818173371b2b6cb626dc05b556"


parameters = {
    "lat": 19.740580,
    "lon": 77.155251,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["hourly"][:12]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today, remember to bring Umbrella",
            from_="+19863004435",
            to="+919309982738"
        )
    print(message.status)