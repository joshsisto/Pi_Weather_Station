from flask import Flask, render_template
from sendEmail import *
from sense_hat import SenseHat

app = Flask(__name__)

@app.route('/')

def index():
    sense = SenseHat()
    sense.clear()

    celcius = round(sense.get_temperature(), 1)
    fahrenheit = round(1.8 * celcius + 32, 1)
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)

    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'], 2)
    y = round(acceleration['y'], 2)
    z = round(acceleration['z'], 2)

    return render_template('weather.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure, x=x, y=y, z=z)

while __name__ == '__main__':
    app.run(host='0.0.0.0')
