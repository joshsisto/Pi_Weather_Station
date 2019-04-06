import datetime
import time
import csv
import os
from math import log
from sense_hat import SenseHat

sense = SenseHat()

RED = [155, 0, 0]
BRED = [255, 0, 0]
ORANGE = [255, 127, 0]
YELLOW = [155, 155, 0]
GREEN = [0, 155, 0]
BLUE = [0, 0, 155]
WHITE = [155, 155, 155]


def get_timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st


def get_sensor_data():
    """Get sensor data from SenseHAT"""
    sense = SenseHat()
    sense.clear()
    celsius = round(sense.get_temperature(), 1)
    fahrenheit = round(1.8 * celsius + 32, 1)
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)
    dewpoint = (round(243.04 * (log(humidity / 100)
                + ((17.625 * celsius) / (243.04 + celsius))) / (17.625 - log(humidity / 100)
                                                                - (17.625 * celsius) / (243.04 + celsius)), 1))
    return [celsius, fahrenheit, humidity, pressure, dewpoint]


def get_xyz():
    """Get orientation data X,Y,Z"""
    sense.clear()
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'], 2)
    y = round(acceleration['y'], 2)
    z = round(acceleration['z'], 2)
    return [x, y, z]


def set_orientation():
    """Set screen orientation based on x,y sensor reading"""
    sense.clear()
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'], 0)
    y = round(acceleration['y'], 0)
    if x == -1:
        sense.set_rotation(90)
    elif y == 1:
        sense.set_rotation(0)
    elif y == -1:
        sense.set_rotation(180)
    else:
        sense.set_rotation(180)


def set_screen_color(fahrenheit):
    """Set screen color based on temperature"""
    if 20 <= fahrenheit <= 80:
        bg_color = BLUE
    elif 81 <= fahrenheit <= 90:
        bg_color = GREEN
    elif 91 <= fahrenheit <= 100:
        bg_color = YELLOW
    elif 101 <= fahrenheit <= 102:
        bg_color = ORANGE
    elif 103 <= fahrenheit <= 104:
        bg_color = RED
    elif 105 <= fahrenheit <= 109:
        bg_color = BRED
    elif 110 <= fahrenheit <= 120:
        bg_color = WHITE
    else:
        bg_color = GREEN
    return bg_color


def log_sensor_data(result_list):
    os.getcwd()
    os.chdir('..')
    os.chdir('src')
    # weather_log = os.path.join(src_dir, 'weather_logs.csv')
    result_list.insert(0, get_timestamp())
    xyz = get_xyz()
    for coordinate in xyz:
        result_list.append(coordinate)
    with open('weather_logs.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(result_list)


def weather():
    """Display SenseHAT data on the 8x8 LED grid"""
    log_sensor_data(get_sensor_data())
    # Display data 5 times before logging it again
    for _ in range(5):
        data_lst = get_sensor_data()
        sense_data = ("Temp. F {} Temp. C {} Hum. {} Press. {} DewPoint {}"
                      .format(data_lst[1], data_lst[0], data_lst[2], data_lst[3], data_lst[4]))
        print(sense_data)
        set_orientation()
        bg_color = set_screen_color(data_lst[1])
        sense.show_message(sense_data, scroll_speed=0.10, back_colour=bg_color, text_colour=WHITE)


while __name__ == '__main__':
    weather()

