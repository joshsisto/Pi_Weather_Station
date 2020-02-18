import datetime
import time
import json
import requests
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


def weather():
    """Display SenseHAT data on the 8x8 LED grid"""
    data_lst = get_sensor_data()
    sense_data = ("Temp. F {} Temp. C {} Hum. {} Press. {} DewPoint {}"
                    .format(data_lst[1], data_lst[0], data_lst[2], data_lst[3], data_lst[4]))
    print(sense_data)
    set_orientation()
    bg_color = set_screen_color(data_lst[1])
    sense.show_message(sense_data, scroll_speed=0.10, back_colour=bg_color, text_colour=WHITE)



# def get_csv_data():
#     day = get_timestamp().split()[0]
#     csv_path = os.path.join(os.path.dirname(__file__) + '/logs/', day + '.csv')
#     with open(csv_path, 'r') as f:
#         # content = f.read()
#         reader = csv.reader(f)
#         for row in reader:
#             print(row)      
#     return row[0]

# # print(get_csv_data())

# csv_content = get_csv_data()
# print()
# print()
# print()
# print(csv_content[0])
# # print(csv_content)

day = get_timestamp().split()[0]
csv_path = os.path.join(os.path.dirname(__file__) + '/logs/', day + '.csv')

def readMyFile(filename):
    dates = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            dates.append(row)
    return dates


weather_stats = readMyFile(csv_path)

# print(weather_stats[-1])

current_stat = weather_stats[-1]
current_aqi = current_stat[10]
current_aqi_num = current_aqi[0]

print(current_stat[9])
print(current_aqi)
print(type(current_aqi))
print(current_aqi_num)

# print(scores)


# while __name__ == '__main__':
    # weather()

