import datetime
import time
import csv
import os
import glob
from math import log
from sense_hat import SenseHat
from weather import get_timestamp

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



day = get_timestamp().split()[0]
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

print(day)
