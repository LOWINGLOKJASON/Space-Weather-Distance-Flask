# ****************************************************************
# Name: Wing Lok LO
# Link: https://replit.com/join/ezqahpujvp-lowinglokjason
# ****************************************************************

# Import necessary libraries
from flask import Flask, render_template
from get_distance import dist
from get_weather import get_weather
from get_address import address
from get_country import country
import requests
import urllib.request
import json

app = Flask('app')

# Define the routes
@app.route('/')
def iss_data():
  data = []
  #ISS current location
  response = requests.get("http://api.open-notify.org/iss-now.json")
  issdata = response.json()
  isslatitude = issdata['iss_position']['latitude']
  isslongitude = issdata['iss_position']['longitude']
  issloc = f"The coordinates of the space station is {isslatitude}, {isslongitude}."
  data.append(issloc)
  #weather
  weather = get_weather(isslatitude, isslongitude)
  weathers = f"The weather below the space station is {weather}°C." 
  data.append(weathers)
  #country
  addresses = address(isslatitude, isslongitude)
  countries = f"The space station is above {addresses}." 
  #water
  if countries == "The space station is above .":
    countries = "The space station is above water."
  else:
    #country info
    countries = countries + country(addresses)
  data.append(countries)
  #distance from the iss
  #my location is on 32 Forest Manor Rd, North York
  #my location and the location of the ISS in lat/lon
  distance = dist(43.771760,-79.344880,isslatitude,isslongitude) 
  #distance
  dist_ = f"You are {distance}km from the ISS."
  data.append(dist_)

  return render_template("index.html",data=data)

app.run(host='0.0.0.0', port=8080)
