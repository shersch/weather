from dotenv import load_dotenv, find_dotenv
import requests
import geocoder
import os
import argparse

load_dotenv(find_dotenv())
address = geocoder.ip('me').address

url = "https://api.openweathermap.org/data/2.5/weather?"


parser = argparse.ArgumentParser()
parser.add_argument("location", type=str, nargs="?", default=address)
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("-c", action="store_true")
group.add_argument("-f", action="store_true")
args = parser.parse_args()

if args.c:
    units = "metric"
elif args.f:
    units = "imperial"
else:
    units = os.getenv("DEF_UNITS")

params = {"q": args.location, "units": units, "appid": os.getenv("APPID")}
r1 = requests.get(url, params=params)
temp = r1.json()['main']
conditions = r1.json()['weather'][0]['description']

print("Location: " + str(r1.json()['name']))
print("Current: " + str(temp['temp']))
print("High: " + str(temp['temp_max']))
print("Low: " + str(temp['temp_min']))
print("Humidity: " + str(temp['humidity']) + "%")
print("Conditions: " + conditions)