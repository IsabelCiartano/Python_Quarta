from microbit import *

while True:
    x = accelerometer.get_x()

    if button_a.was_pressed():
        print("SHOOT")

    print(x)

    sleep(20)