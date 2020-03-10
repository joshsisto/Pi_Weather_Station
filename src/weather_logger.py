import datetime
import time
import json
import requests
import csv
import os
from sense_hat import SenseHat
from math import log

sense = SenseHat()

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
    try:        
        dewpoint = (round(243.04 * (log(humidity / 100)
                    + ((17.625 * celsius) / (243.04 + celsius))) / (17.625 - log(humidity / 100)
                                                                    - (17.625 * celsius) / (243.04 + celsius)), 1))
    except:
        dewpoint = 'broken'
    return [celsius, fahrenheit, humidity, pressure, dewpoint]


def get_xyz():
    """Get orientation data X,Y,Z"""
    sense.clear()
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'], 2)
    y = round(acceleration['y'], 2)
    z = round(acceleration['z'], 2)
    return [x, y, z]


def log_sensor_data(result_list):
    """Log sensor data"""
    day = get_timestamp().split()[0]
    src_dir = os.path.dirname(os.path.realpath(__file__))
    w_log = os.path.join(src_dir + '/logs/', day + '.csv')
    result_list.insert(0, get_timestamp())
    xyz = get_xyz()
    for coordinate in xyz:
        result_list.append(coordinate)
    # Get weather and AQI and append
    weather_api = get_weather()
    result_list.append(weather_api)
    aqi_api = get_aqi()
    result_list.append(aqi_api)
    
    with open(w_log, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(result_list)


def convert_time(time_string):
    return time.ctime(time_string)


weather_url = 'https://api.darksky.net/forecast/cd562f431296f113d3a618a7ea1d94ef/38.561936,-121.423951'
air_url = 'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=95817&distance=1&API_KEY=F62EEA9E-1177-456C-89B2-94CA763972C6'


def get_json(url):
    resp = requests.get(url)
    data = resp.json()
    return data


def get_aqi():
    air_json = get_json(air_url)
    aqi = air_json[0]['AQI']
    air_status = air_json[0]['Category']['Name']
    air_list = []
    air_list.append(aqi)
    air_list.append(air_status)
    return air_list

# print(get_aqi())


def get_weather():
    """ Returns a list of the weather
    [Temp, ] """
    data = get_json(weather_url)
    current_weather = data['currently']
    daily_sum = current_weather['summary']
    current_temp = current_weather['temperature']
    forecast = data['daily']['summary']
    weather_list = []
    weather_list.append(current_temp)
    weather_list.append(daily_sum)
    weather_list.append(forecast)
    file_path = '/home/pi/Pi_Weather_Station/src/weather.json'
    with open(file_path, 'w', encoding='utf-8') as output:
        json.dump(data, output, ensure_ascii=False, indent=4)
    return weather_list

# print(get_weather())


log_sensor_data(get_sensor_data())

