import json
import urllib
import urllib.request
from formulas import toFahrenheit, toCelsius

# A place to keep the API search formula


def searchCity(city):
    api_key = '66e64fc4eb7e73b64c9e5eeccfcaed4c'

    # API Call from OpenWeather returns JSON of City data if found 404 if not
    source = urllib.request.urlopen(
        'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()

    # Convert JSON data to dictionary
    list_of_data = json.loads(source)

    # Data for loading variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": toFahrenheit(list_of_data['main']['temp']) + ' F',
        "temp_cel": toCelsius(list_of_data['main']['temp']) + ' C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname": str(city),
        # cityid is used when findID function is active
        # "cityid": findID(city)
    }
    # Use data list to render info in index.html
    return data
