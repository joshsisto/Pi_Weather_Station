import datetime
import time
import json
import requests
import csv
import os
from math import log
from sense_hat import SenseHat

from flask import Flask, request, render_template
from sendEmail import send_email
from sense_hat import SenseHat
import time
import os
import csv
import ast
import tablib
import pandas as pd
import json

sense = SenseHat()

RED = [155, 0, 0]
BRED = [255, 0, 0]
ORANGE = [255, 127, 0]
YELLOW = [155, 155, 0]
GREEN = [0, 155, 0]
BLUE = [0, 0, 155]
PURPLE = [128, 0, 128]
WHITE = [155, 155, 155]
BRIGHT_WHITE = [255, 255, 255]



dataset = tablib.Dataset()

def convert_epoch(epoch_time):
    converted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))
    return converted_time


def epoch_to_day(epoch_time):
    converted_time = time.strftime('%A', time.localtime(epoch_time))
    return converted_time


def get_csv_data():
    """Open the daily csv log and return the content"""
    csv_list = []
    day = get_timestamp().split()[0]
    csv_path = os.path.join(os.path.dirname(__file__) + '/logs/', day + '.csv')
    # csv_path = '/home/pi/Pi_Weather_Station/src/logs/' + day + '.csv'
    with open(csv_path, 'r') as csv_file:
        # content = f.read()
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # print(row)
            csv_list.append(row)
    return csv_list

# print(get_csv_data())

def get_dark_sky():
    """Read the most recent dark sky log and return a list of the stats"""
    csv_content = get_csv_data()
    most_recent = csv_content[-1]
    dark_sky_string = most_recent[9]
    dark_sky_list = dark_sky_string.strip('][').split(', ')
    ds_temp = dark_sky_list[0]
    ds_cond = dark_sky_list[1].strip("'")
    ds_fore = dark_sky_list[2].strip("'")
    return [ds_temp, ds_cond, ds_fore]

# print(get_dark_sky())

def get_gov_aqi():
    """Read the most recent aqi log and return the stats"""
    csv_content = get_csv_data()
    most_recent = csv_content[-1]
    aqi_string = most_recent[10]
    aqi_list = aqi_string.strip('][').split(', ')
    aqi = aqi_list[0]
    air_cond = aqi_list[1].strip("'")
    return [aqi, air_cond]

# print(get_gov_aqi())



def get_timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st



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
    if 20 <= int(fahrenheit) <= 80:
        bg_color = BLUE
    elif 81 <= int(fahrenheit) <= 90:
        bg_color = GREEN
    elif 91 <= int(fahrenheit) <= 100:
        bg_color = YELLOW
    elif 101 <= int(fahrenheit) <= 102:
        bg_color = ORANGE
    elif 103 <= int(fahrenheit) <= 104:
        bg_color = RED
    elif 105 <= int(fahrenheit) <= 109:
        bg_color = BRED
    elif 110 <= int(fahrenheit) <= 120:
        bg_color = WHITE
    else:
        bg_color = GREEN
    return bg_color


def weather():
    """Display SenseHAT data on the 8x8 LED grid"""
    data_lst = get_csv_data()
    sense_data = ("{}        AQI:{}        "
                    .format(data_lst[9], data_lst[-1]))
    print(sense_data)
    set_orientation()

    # bg_color = set_screen_color(data_lst[9][0])
    sense.show_message(sense_data, scroll_speed=0.10, back_colour=PURPLE, text_colour=BRIGHT_WHITE)


while __name__ == '__main__':
    try:
        weather()
    except KeyboardInterrupt:
        # Clear the sense hat when manually interrupted
        sense.clear()
        exit()






