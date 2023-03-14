import RPi.GPIO as GPIO
import time

# Use BCM GPIO references
GPIO.setmode(GPIO.BCM)

# set GPIO 24 as input
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    # read the state of the button on GPIO 24
    button_state = GPIO.input(24)

    # check if the button is pressed
    if button_state == False:
        print("Button Pressed")
        time.sleep(0.2)

    # check if the button is not pressed
    if button_state == True:
        print("Button Not Pressed")
        time.sleep(0.2)

GPIO.cleanup()

