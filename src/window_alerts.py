import datetime
import time
import csv
import os
import ast
import glob
import json
from math import log
from sense_hat import SenseHat
from weather import get_timestamp
from sendText import *


def get_csv_data():
    """Open the daily csv log and return the content"""
    global csv_path
    csv_list = []
    day = get_timestamp().split()[0]
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/logs/', day + '.csv')
    # csv_path = '/home/pi/Pi_Weather_Station/src/logs/' + day + '.csv'
    with open(csv_path, 'r') as csv_file:
        # content = f.read()
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # print(row)
            csv_list.append(row)
    return csv_list

get_csv_data()

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

# print(os.path.basename(csv_path))
# print(csv_path[:-3] + 'alert')



def check_min():
    global current_temp
    global daily_high_temp
    try:
        # alert_cont = read_alert()
        with open('/home/pi/Pi_Weather_Station/src/weather.json') as json_file:
            data = json.load(json_file)
            today_temp_hi = data['daily']['data'][0]['temperatureHigh']
            minimum_temp = 74
            current_temp = get_dark_sky()[0]
            current_temp = float(current_temp)
            daily_high_temp = float(today_temp_hi)
            if daily_high_temp >= 80 and current_temp >= 74:
                print('It is 74 degrees or warmer! Time to close the windows')
                return True
            else:
                print('Temperature is within limit set')
                return False
    except:
        print('That did not work.')
        print('probably did not have a value set for minimum temp')
        print(current_temp, daily_high_temp)
        

alert_file_path = csv_path[:-3] + 'alert'

if os.path.exists(alert_file_path) == False:
    print('no alert file detected')
    if check_min() == True:
        print("Temp reached! creating alert flag")
        alert_flag = open(alert_file_path, 'w+')
        print("Sending Text")
        email_message = 'It is {} outside with a High of {}. You should close the windows to keep the house cool. Love you!'.format(current_temp, daily_high_temp)
        print(email_message)
        send_email(email_message)

print('need to print something')
print(alert_file_path)