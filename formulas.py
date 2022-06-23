# A place to keep any necessary formulas


# Converts Kelvin to Celsius
def toCelsius(temp):
    return str(round(float(temp) - 273.16, 1))


# Converts Kelvin to Fahrenheit
def toFahrenheit(temp):
    inf = round((float(temp) - 273.16), 2) * 1.8 + 32
    return str(round(inf, 0))
