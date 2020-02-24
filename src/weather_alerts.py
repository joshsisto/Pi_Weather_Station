import datetime
import time
import csv
import os
import ast
import glob
from math import log
from sense_hat import SenseHat
from weather import get_timestamp
from sendEmail import *


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


def get_gov_aqi():
    """Read the most recent aqi log and return the stats"""
    csv_content = get_csv_data()
    most_recent = csv_content[-1]
    aqi_string = most_recent[10]
    aqi_list = aqi_string.strip('][').split(', ')
    aqi = aqi_list[0]
    air_cond = aqi_list[1].strip("'")
    return [aqi, air_cond]


def read_alert():
    file_path = '/home/pi/Pi_Weather_Station/src/alerts.txt'
    with open(file_path, 'r') as input:
        s = input.read()
        whip = ast.literal_eval(s)
    return whip


def check_max():
    try:    
        alert_cont = read_alert()
        maximum_temp = int(alert_cont['max_temp'])
        current_temp = get_dark_sky()[0]
        current_temp = float(current_temp)
        if current_temp >= maximum_temp:
            print('Current temperature exceeds maximum temperature threshhold set')
            print('Check https://pi.sisto.solutions/alerts')
            return True
        else:
            print('Temperature is within limit set')
            return False
    except:
        print('That did not work.')
        print('probably did not have a value set for maximum temp')


def check_min():
    try:
        alert_cont = read_alert()
        minimum_temp = int(alert_cont['min_temp'])
        current_temp = get_dark_sky()[0]
        current_temp = float(current_temp)            
        if current_temp <= minimum_temp:
            print('Current temperature exceeds minimum temperature threshhold set')
            print('Check https://pi.sisto.solutions/alerts')
            return True
        else:
            print('Temperature is within limit set')
            return False
    except:
        print('That did not work.')
        print('probably did not have a value set for minimum temp')


def check_air():
    try:
        alert_cont = read_alert()
        maximum_aqi = int(alert_cont['aqi_max'])
        current_aqi = get_gov_aqi()[0]
        current_aqi = float(current_aqi)            
        if current_aqi >= maximum_aqi:
            print('Current AQI exceeds maximum threshhold set')
            print('Check https://pi.sisto.solutions/alerts')
            return True
        else:
            print('AQI is within limit set')
            return False
    except:
        print('That did not work.')
        print('probably did not have a value set for aqi')


if check_max() == True:
    send_email('Max Temp Reached', 'Check https://pi.sisto.solutions')


if check_min() == True:
    send_email('Min Temp Reached', 'Check https://pi.sisto.solutions')


if check_air() == True:
    send_email('AQI max threshold crossed', '😷')

