# Project: Adventure Weather
# Purpose Details: Group 3 Capstone Project
# Course: IST 440W
# Authors: Craig Freiwald, Sabrina Matteoli, Zachary Huff
# Date Developed: 14 June 2022
# Last Date Changed: 23 June 2022
# Revision #: 4

import os

from flask import Flask, render_template, request, session

from searchFunction import searchCity

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'


# Set routes for city request
@app.route('/weather', methods=['POST'])
def weather():
    # Default City
    city = 'Miami'
    return render_template('weather.html', data=searchCity(city))


@app.route('/searchresults', methods=['POST'])
def search():
    city = request.form['city']

    # Use data list to render info in index.html
    return render_template('weather.html', data=searchCity(city))


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return do_admin_login()


@app.route('/home', methods=['POST'])
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
