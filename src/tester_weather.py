import datetime
import time
import csv
import os
import ast
import glob
from math import log
from sense_hat import SenseHat
from weather import get_timestamp


def get_timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st

# test_list = ['boom', 'bam', 0]

test_dict = {'max' : '45', 'min' : '45', 'AQI' : 0}

def save_alert(result_dict):
    """Take a list and save it as a csv"""
    # src_dir = os.path.dirname(os.path.realpath(__file__))
    # w_log = os.path.join(src_dir + '/logs/', day + '.csv')
    file_path = '/home/pi/Pi_Weather_Station/src/alerts.txt'
    with open(file_path, 'w') as output:
        output.write(str(result_dict))

# save_alert(test_dict)

def read_alert():
    file_path = '/home/pi/Pi_Weather_Station/src/alerts.txt'
    with open(file_path, 'r') as input:
        s = input.read()
        whip = ast.literal_eval(s)
    return whip

# print(read_alert())

alert_cont = read_alert()

print(alert_cont)
print(type(alert_cont))
print(alert_cont['max'])


# def get_timestamp():
#     ts = time.time()
#     st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#     return st

# # print(get_timestamp())
# # get_timestamp()

# ts = get_timestamp().split()
# print(type(ts))
# # ts = ts.split()
# print(ts[0])

# w_log = ts[0]

# with open(w_log, 'a', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow('text')



# day = get_timestamp().split()[0]
# src_dir = os.path.dirname(os.path.realpath(__file__))
# w_log = os.path.join(src_dir, day + '.csv')
# result_list.insert(0, get_timestamp())
# xyz = get_xyz()
# for coordinate in xyz:
    # result_list.append(coordinate)
# with open(w_log, 'a', newline='') as csv_file:
    # writer = csv.writer(csv_file)
    # writer.writerow(result_list)

# print(content)

# print(day)

# def get_csv_data():
#     """Open the daily csv log and return the content"""
#     csv_list = []
#     day = get_timestamp().split()[0]
#     # csv_path = os.path.join(os.path.dirname(__file__) + '/logs/', day + '.csv')
#     csv_path = '/home/pi/Pi_Weather_Station/src/logs/' + day + '.csv'
#     with open(csv_path, 'r') as csv_file:
#         # content = f.read()
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         for row in csv_reader:
#             # print(row)
#             csv_list.append(row)
#     return csv_list

# # print(get_csv_data())

# def get_dark_sky():
#     """Read the most recent dark sky log and return a list of the stats"""
#     csv_content = get_csv_data()
#     most_recent = csv_content[-1]
#     dark_sky_string = most_recent[9]
#     dark_sky_list = dark_sky_string.strip('][').split(', ')
#     ds_temp = dark_sky_list[0]
#     ds_cond = dark_sky_list[1].strip("'")
#     ds_fore = dark_sky_list[2].strip("'")
#     return [ds_temp, ds_cond, ds_fore]

# print(get_dark_sky())

# def get_gov_aqi():
#     """Read the most recent aqi log and return the stats"""
#     csv_content = get_csv_data()
#     most_recent = csv_content[-1]
#     aqi_string = most_recent[10]
#     aqi_list = aqi_string.strip('][').split(', ')
#     aqi = aqi_list[0]
#     air_cond = aqi_list[1].strip("'")
#     return [aqi, air_cond]

# print(get_gov_aqi())
