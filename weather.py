from flask import Flask, render_template, request, abort
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

app = Flask(__name__)

# converts kelvin returned from API to Celsius
def toCelsius(temp):
    return str(round(float(temp) - 273.16, 1))

# converts kelvin returned from API to Fahrenheit
def toFahrenheit(temp):
    inf = round((float(temp) - 273.16), 2) * 1.8 + 32
    return str(round(inf, 0))


@app.route('/', methods=['POST', 'GET'])
def weather():
    api_key = '66e64fc4eb7e73b64c9e5eeccfcaed4c'
    if request.method == 'POST':
        city = request.form['city']
        # cityid = request.form['cityid']
    else:
        # default city
        city = 'Miami'

    # source contain json data from api
    try:
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key).read()
    except:
        return abort(404)
    # converting json data to dictionary

    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": toFahrenheit(list_of_data['main']['temp']) + ' F',
        "temp_cel": toCelsius(list_of_data['main']['temp']) + ' C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname": str(city),
        # "cityid": str(cityid)
    }
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
