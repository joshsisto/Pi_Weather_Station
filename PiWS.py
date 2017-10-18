import time
import datetime
import csv
import multiprocessing
from sendEmail import *
from math import log
from flask import Flask, render_template
from sense_hat import SenseHat

sendEmail('Hot Temp Alert', 'Crazy message body')

app = Flask(__name__)

def weather():
    sense = SenseHat()
    sense.clear()

    celcius = round(sense.get_temperature(), 1)
    fahrenheit = round(1.8 * celcius + 32, 1)
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)
    dewpoint = round(243.04 * (log(humidity / 100) + ((17.625 * celcius) / (243.04 + celcius))) / (17.625 - log(humidity / 100) - (17.625 * celcius) / (243.04 + celcius)), 1)

    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'], 0)
    y = round(acceleration['y'], 0)
    z = round(acceleration['z'], 0)

    if x == -1:
        sense.set_rotation(90)
    elif y == 1:
        sense.set_rotation(0)
    elif y == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(180)

    if fahrenheit > 20 and fahrenheit < 80:
        bg_color = [0, 0, 155]  # blue
    if fahrenheit > 81 and fahrenheit < 90:
        bg_color = [0, 155, 0]  # Green
    if fahrenheit > 91 and fahrenheit < 100:
        bg_color = [155, 155, 0]  # Yellow
    if fahrenheit > 101 and fahrenheit < 102:
        bg_color = [255, 127, 0]  # Orange
    if fahrenheit > 103 and fahrenheit < 104:
        bg_color = [155, 0, 0]  # Red
    if fahrenheit > 105 and fahrenheit < 109:
        bg_color = [255, 0, 0]  # Bright Red
    if fahrenheit > 110 and fahrenheit < 120:
        bg_color = [155, 155, 155]  # White
    else:
        bg_color = [0, 155, 0]  # Green

    result = ' Temp. F ' + str(fahrenheit) + ' Temp. C ' + str(celcius) + ' Hum. ' + str(humidity) + ' Press. ' + str(pressure) + ' DewPoint ' + str(dewpoint)
    print(result)
    result_list = [(datetime.datetime.now(), celcius, fahrenheit, humidity, pressure, dewpoint)]
    with open('weather_logs.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(result_list)
    for x in range(5):
        sense.show_message(result, scroll_speed=0.10, back_colour=bg_color, text_colour=[155, 155, 155])

@app.route('/')

def index():
    sense = SenseHat()
    sense.clear()

    celcius = round(sense.get_temperature(), 1)
    fahrenheit = round(1.8 * celcius + 32, 1)
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)
    dewpoint = round(243.04 * (log(humidity / 100) + ((17.625 * celcius) / (243.04 + celcius))) / (17.625 - log(humidity / 100) - (17.625 * celcius) / (243.04 + celcius)), 1)

    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'], 1)
    y = round(acceleration['y'], 1)
    z = round(acceleration['z'], 1)

    return render_template('weather.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure, dewpoint=dewpoint, x=x, y=y, z=z)

while __name__ == '__main__':
    weather()
    #app.run(host='0.0.0.0')
