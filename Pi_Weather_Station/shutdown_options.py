from sense_hat import SenseHat
from time import sleep
import os

# Generic colors for re-use
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (0, 0, 0)

sense = SenseHat()

# For the Sense HAT joystick, up is towards the GPIO pins and down is away from them

while True:
    event = sense.stick.wait_for_event()
    if (event.action == "held" and event.direction == "up"):
        sense.show_message("Rebooting", text_colour=red)
        os.system('sudo shutdown -r now')
    elif (event.action == "held" and event.direction == "down"):
        sense.show_message("Shutdown", text_colour=blue)
        os.system('sudo shutdown -h now')
    else:
        # General handling for debugging
        print("The joystick was {} {}".format(event.action, event.direction))

    sleep(0.1)
