# Project: Adventure Weather
# Purpose Details: Group 3 Capstone Project
# Course: IST 440W
# Authors: Craig Freiwald, Sabrina Matteoli, Zachary Huff
# Date Developed: 14 June 2022
# Last Date Changed: 23 June 2022
# Revision #: 4

import json
import os
import urllib.request
from flask import Flask, flash, render_template, request, session, abort


app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'


# Converts Kelvin to Celsius
def toCelsius(temp):
    return str(round(float(temp) - 273.16, 1))


# Converts Kelvin to Fahrenheit
def toFahrenheit(temp):
    inf = round((float(temp) - 273.16), 2) * 1.8 + 32
    return str(round(inf, 0))


# @app.route('/weather', methods={'POST'})
# def weather():
#     if not session.get('logged_in'):
#         return render_template('login.html')
#     else:
#         return pingWeather()


# Set routes for city request
@app.route('/weather', methods=['POST', 'GET'])
def weather():
    api_key = '66e64fc4eb7e73b64c9e5eeccfcaed4c'

    if request.method == 'POST':
        # default city
        city = 'Miami'
    elif request.method == 'GET':
        city = request.form['city']

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
    return render_template('weather.html', data=data)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return do_admin_login()


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['logged_in'] = True
        return weather()
    else:
        return home()


@app.errorhandler(500)
def error_500(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
