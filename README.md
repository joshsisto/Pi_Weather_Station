## Pi_Weather_Station: Weather Station Using Raspberry Pi and Sense HAT

### Description
These scripts use a 
[Raspberry Pi](http://amzn.to/2yB8HcM) with a 
[Sense HAT](http://amzn.to/2xS8PFX) 
to monitor temperature, humidity, pressure, and orientation. It displays the data taken by the sense HAT sensors and prints them to the sense HAT 8x8 LED matrix and makes the data available via the web browser using Flask. It also logs the data to a .csv file.

### Getting Started
On your raspberry pi with sense HAT run the commands lines below

    `sudo apt-get update`
    `sudo apt-get upgrade`
    `git clone https://github.com/llamafarmer/Pi_Weather_Station.git`

Next you will need to install the packages needed for the scripts to execute

    `sudo apt-get install python3-flask`
    `sudo apt-get install sense-hat`

You then need to change directories to the newly downloaded repository and start the python scripts

    `cd Pi_Weather_Station`
    `python3 weather.py`
    `python3 web_app.py`

The 8x8 LED matrix should light up and begin scrolling sensor information. You can also view the sensor information using the web browser and pointing it to port 5000 of the raspberry pi. https://PiHAT:5000

To execute these scripts automatically... create .sh

These scripts are based off my this original project - https://github.com/llamafarmer/Pi/blob/master/MWS.py

Links/sources: https://github.com/kronebone/Cold-Room, https://thepi.io/how-to-set-up-a-raspberry-pi-weather-station-using-the-sense-hat/, https://veekaybee.github.io/2017/09/26/python-packaging/

### todo
add joystick functionality

add video ([Pi Camera](http://amzn.to/2xSoF3w))

improve web interface (buttons/user input)

Allow user to create email alerts

Screenshots

Quick Start - Create .sh file to launch .py scripts
