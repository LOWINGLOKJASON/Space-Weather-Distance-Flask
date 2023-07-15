import urllib.request
import json

def get_weather(lat, lon):
    """
    Get the weather at a given location
    """
    key = 'fe8864f0805d25db6c7d08959d89dd60'  # enter api key
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    request = urllib.request.urlopen(url)
    # extract the temperature
    result = json.loads(request.read())['main']['temp'] 
    return round(result - 273.15, 1)