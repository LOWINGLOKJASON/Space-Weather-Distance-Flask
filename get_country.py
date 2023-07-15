import urllib.request
import json

def country(code):
  url = f'https://restcountries.com/v3.1/alpha/{code}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  # extract the country name, flag and population
  f_result = f"{result[0]['name']['common']} {result[0]['flag']} is a country with {result[0]['population']} population."
  return f_result