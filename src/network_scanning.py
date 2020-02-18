#python

import os
import subprocess
import ipaddress
import socket

# my_hostname = socket.gethostbyname(socket.gethostname())
# print(f'host IP:{my_hostname}')
# print('host IP: {}'.format(my_hostname))

def check_host_up(hostname):
    ping_host = subprocess.Popen(['ping', '-c', '3', hostname])
    ping_output = ping_host.communicate()
    host_alive = ping_host.returncode
    if host_alive == 0:
        print('\n{} is up\n'.format(hostname))
    else:
        print('\n{} not reachable\n'.format(hostname))

check_host_up('192.168.88.1')

# def nmap_scan(nmap_target):
    # scan_target = subprocess.call(['nmap', nmap_target])
    # print(scan_target)

# nmap_scan('joshsisto.com')

# myCmd = 'nmap joshsisto.com > out.txt'
# os.system.myCmd

def nmap_scan(nmap_target):
    scan_target = os.popen('nmap {}'.format(nmap_target)).read()
    print(scan_target)
    # save the scan data nmap_target.DATE

nmap_scan('thebananastand.com')
