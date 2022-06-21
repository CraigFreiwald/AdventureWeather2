# Project: Adventure Weather
# Purpose Details: Group 3 Capstone Project
# Course: IST 440W
# Authors: Craig Freiwald, Sabrina Matteoli, Zachary Huff
# Date Developed: 14 June 2022
# Last Date Changed: 21 June 2022
# Revision #: 3


# Import Flask utilities
from flask import Flask, render_template, request, abort
# Import JSON to use json.loads() to add API return data to dictionary
import json
# Import urllib.request to make a request to api
import urllib.request

# Name to identify app when running
app = Flask(__name__)


# Converts Kelvin to Celsius
def toCelsius(temp):
    return str(round(float(temp) - 273.16, 1))


# Converts Kelvin to Fahrenheit
def toFahrenheit(temp):
    inf = round((float(temp) - 273.16), 2) * 1.8 + 32
    return str(round(inf, 0))


# Possibly deprecated function - keeping for future use
# # finds requested city id in cit.list.json
# def findID(city):
#     input_file = open('city.list.json')
#     json_array = json.load(input_file)
#     city_list = []
#
#     for item in json_array:
#         city_name = {"name": None, "id": None, 'name': item['name'], 'id': item['id']}
#         city_list.append(city_name)

# Set routes for city request
@app.route('/', methods=['POST', 'GET'])
def weather():
    api_key = '66e64fc4eb7e73b64c9e5eeccfcaed4c'
    if request.method == 'POST':
        city = request.form['city']
    else:
        # default city
        city = 'Miami'

    # API Call from OpenWeather returns JSON of City data if found 404 if not
    try:
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()
    except:
        return abort(404)

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
    return render_template('index.html', data=data)


# Run application (in debug mode)
if __name__ == '__main__':
    app.run(debug=True)
