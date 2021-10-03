from dotenv import load_dotenv, find_dotenv
import requests
import sys
import geocoder
import os

load_dotenv(find_dotenv())
g = geocoder.ip('me')

url = "https://api.openweathermap.org/data/2.5/weather?"

try:
    if len(sys.argv[1]) > 1:
        city = sys.argv[1]
        units = "imperial"
    elif len(sys.argv[1]) == 1:
        if sys.argv[1].lower() == "c":
            units = "metric"
        elif sys.argv[1].lower() == "f":
            units = "imperial"
        try:
            if len(sys.argv[2]) > 1:
                city = sys.argv[2]
        except:
            city = g.city + "," + g.state + "," + g.country
except:
    city = g.city + "," + g.state + "," + g.country
    units = "imperial"

params = {"q": city, "units": units, "appid": os.getenv("APPID")}
r1 = requests.get(url, params=params)
temp = r1.json()['main']
conditions = r1.json()['weather'][0]['description']

print("Location: " + str(r1.json()['name']))
print("Current: " + str(temp['temp']))
print("High: " + str(temp['temp_max']))
print("Low: " + str(temp['temp_min']))
print("Humidity: " + str(temp['humidity']) + "%")
print("Conditions: " + conditions)