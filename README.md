## Pi_Weather_Station: Weather Station Using Raspberry Pi and Sense HAT
Python 3.4.2 | flask 0.10.1 | sense_hat 2.2.0

[Running Here](https://pi.sisto.solutions/)

<img src="/images/IMG_0705.jpg" alt="Pi with HAT" style="width: 200px;"/>

### Description
These scripts use a
[Raspberry Pi](http://amzn.to/2yB8HcM) with a
[Sense HAT](http://amzn.to/2xS8PFX)
to monitor temperature, humidity, pressure, and orientation. The sensor
information is displayed on the sense HAT 8x8 LED matrix, and via the web
browser using [flask](http://flask.pocoo.org/).

### Getting Started
On your raspberry pi with sense HAT run the command lines below

    sudo apt-get update
    sudo apt-get upgrade
    git clone https://github.com/joshsisto/Pi_Weather_Station.git

Next you will need to install the packages needed for the scripts to execute

    sudo apt-get install python3-flask
    sudo apt-get install sense-hat

To test everything is working change directories to the newly downloaded repo
and execute using Python 3

    cd Pi_Weather_Station
    python3 weather.py
    python3 web_app.py

The 8x8 LED matrix should light up and begin scrolling sensor information. You
can also view the sensor information using the web browser and pointing it to
port 5000 of the raspberry pi.

<img src="/images/animated.gif" alt="Pi HAT LED" style="width: 200px;"/>

<img src="/images/Pi_Web.PNG" alt="Web Screenshot" style="width: 200px;"/>

To execute these scripts automatically you need to update the bash scripts in
the utils folder and make them executable

First change directories to the utils folder and update the bash scripts to
point to your python scripts

    cd utils
    nano launch_weather.sh
    nano launch_web_app.sh

Then make them executable

    sudo chmod +x launch_weather.sh
    sudo chmod +x launch_web_app.sh

Test the files

    ./launch_weather.sh
    ./launch_web_app.sh

Lastly add them to cron

    sudo crontab -e
    @reboot /home/pi/Pi_Weather_Station/utils/launch_weather.sh
    @reboot /home/pi/Pi_Weather_Station/utils/launch_web_app.sh

ctrl+x to exit and y to save. Then enter the command below to reboot

    sudo reboot -h now

Your raspberry pi should reboot and execute both scripts on startup

### todo
+ ~~add joystick functionality~~ thanks @atbPy
+ ~~add video ([Pi Camera](http://amzn.to/2xSoF3w))~~ see [`Hummingbird_Watcher`](https://github.com/llamafarmer/Hummingbird_Watcher)
+ ~~improve web interface (buttons/user input)
+ ~~Allow user to create email alerts
+ Keep improving app!
## Copyright and License
Copyright (c) 2017 Josh Sisto [MIT License](/LICENSE)
