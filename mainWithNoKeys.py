import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "xxx"
ACCOUNT_SID = "xxx"
AUTH_TOKEN = "xxx"
MY_LAT = 53.349804
MY_LONG = -6.260310

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minute,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It is going to rain today, Bring an umbrella ☂",
        from_='+19135213467',
        to='+353838247120'
    )
print(message.status)

