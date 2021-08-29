import requests
from twilio.rest import Client
account_sid = "AC0a08ddb789267b98da954d771b447f58"
auth_token ="6103ca4494ae015a7005b3e2e656074b"

api_key = "28b97eed4cd240a19c6b79930878143a"

parameters = {
    "lat":57.477772,
    "lon":-4.224721,
    "appid":api_key,
    "exclude":"current,minutely,daily"}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.status_code)
data= response.json()
weather_slice = data["hourly"][:12]

will_rain= False
for hr_data in weather_slice:
    condition = (hr_data["weather"][0]["id"])
    if int(condition)<700:
        will_rain = True
if will_rain=="True":
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Take your umberella today✌️✌️",
        from_='+13104947099',
        to="+918173873366")
    print(message.status)

# print(data["hourly"][0]["weather"][0]["id"])

