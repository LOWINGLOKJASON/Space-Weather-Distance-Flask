import urllib.request
import json

def address(lat, lon):
  key = 'DnNrBG4kI0kKHA04ez2YqBONrP7EhprE' # enter api key
  url = f'http://www.mapquestapi.com/geocoding/v1/reverse?key={key}&location={lat},{lon}&includeRoadMetadata=true&includeNearestIntersection=true'
  request = urllib.request.urlopen(url)
  # extract the country code
  result = json.loads(request.read())['results'][0]['locations'][0]['adminArea1']
    
  return result


