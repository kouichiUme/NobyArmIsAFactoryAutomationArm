
# -*- coding: utf-8 -*-
import pigpio
import time

# X direction

gpio_pin_X_orange = 12
gpio_pin_X_yellow = 16
gpio_pin_X_brown = 20
gpio_pin_X_black = 21

# Y direction (height)

gpio_pin_Y_orange = 15
gpio_pin_Y_yellow = 25
gpio_pin_Y_brown = 8
gpio_pin_Y_black = 7

# Z direction (height)

gpio_pin_Z_orange = 2
gpio_pin_Z_yellow = 3
gpio_pin_Z_brown = 4
gpio_pin_Z_black = 14
pi = pigpio.pi()


def main():
    print("start pigpio")


    pi.set_mode(gpio_pin_X_orange, pigpio.OUTPUT)
    pi.set_mode(gpio_pin_X_yellow, pigpio.OUTPUT)
    pi.set_mode(gpio_pin_X_brown, pigpio.OUTPUT)
    pi.set_mode(gpio_pin_X_black, pigpio.OUTPUT)
    time.sleep(5)
    startCWRotate(True)
    startYCWRotate(True)
    startZCWRotate(True)
    startCCWRotate(True)


def startCWRotate(startStop):
# X is black
# X_ is orange
# Y is brown
# Y_ is yellow
# 2 phase
# 1 step 3.75 degree
#       1               2
# X     on  on off off  on on off
# X_    off on on  off  off on on
# Y     off off on on   off off on
# Y_    on off off on   on off off
# clockwise
    i = 0
    while startStop and i < 30:
        pi.write(gpio_pin_X_black, 1)
        pi.write(gpio_pin_X_yellow, 0)
        time.sleep(0.1)

        pi.write(gpio_pin_X_orange, 1)
        time.sleep(0.1)
        pi.write(gpio_pin_X_black, 0)
        time.sleep(0.1)
        pi.write(gpio_pin_X_brown, 1)
        time.sleep(0.1)
        pi.write(gpio_pin_X_orange, 0)
        time.sleep(0.1)
        pi.write(gpio_pin_X_yellow, 1)
        time.sleep(0.1)
        pi.write(gpio_pin_X_brown, 0)
        time.sleep(0.1)
        i += 1
#

def startYCWRotate(startStop):
# X is black
# X_ is orange
# Y is brown
# Y_ is yellow
# 2 phase
# 1 step 3.75 degree
#       1               2
# X     on  on off off  on on off
# X_    off on on  off  off on on
# Y     off off on on   off off on
# Y_    on off off on   on off off
# clockwise
    i = 0
    while startStop and i < 30:
        pi.write(gpio_pin_Y_black, 1)
        pi.write(gpio_pin_Y_yellow, 0)
        time.sleep(0.1)

        pi.write(gpio_pin_Y_orange, 1)
        time.sleep(0.1)
        pi.write(gpio_pin_Y_black, 0)
        time.sleep(0.1)
        pi.write(gpio_pin_Y_brown, 1)
        time.sleep(0.1)
        pi.write(gpio_pin_Y_orange, 0)
        time.sleep(0.1)
        pi.write(gpio_pin_Y_yellow, 1)
        time.sleep(0.1)
        pi.write(gpio_pin_Y_brown, 0)
        time.sleep(0.1)
        i += 1
#

def startZCWRotate(startStop):
# X is black
# X_ is orange
# Y is brown
# Y_ is yellow
# 2 phase
# 1 step 3.75 degree
#       1               2
# X     on  on off off  on on off
# X_    off on on  off  off on on
# Y     off off on on   off off on
# Y_    on off off on   on off off
# clockwise
    i = 0
    while startStop and i < 30:
        pi.write(gpio_pin_Z_black, 1)
        pi.write(gpio_pin_Z_yellow, 0)
        time.sleep(0.1)

        pi.write(gpio_pin_Z_orange, 1)
        time.sleep(0.1)
        pi.write(gpio_pin_Z_black, 0)
        time.sleep(0.1)
        pi.write(gpio_pin_Z_brown, 1)
        time.sleep(0.1)
        pi.write(gpio_pin_Z_orange, 0)
        time.sleep(0.1)
        pi.write(gpio_pin_Z_yellow, 1)
        time.sleep(0.1)
        pi.write(gpio_pin_Z_brown, 0)
        time.sleep(0.1)
        i += 1
#



def startCCWRotate(startStop):
# counter clock wise
    i = 0
    while startStop and i < 30:
        pi.write(gpio_pin_X_brown,0)
        time.sleep(0.1)
        pi.write(gpio_pin_X_yellow,1)
        time.sleep(0.1)
        pi.write(gpio_pin_X_orange,0)
        time.sleep(0.1)
        pi.write(gpio_pin_X_brown,1)
        time.sleep(0.1)
        pi.write(gpio_pin_X_black,0)
        time.sleep(0.1)
        pi.write(gpio_pin_X_orange,1)
        time.sleep(0.1)
        pi.write(gpio_pin_X_yellow,0)
        time.sleep(0.1)
        pi.write(gpio_pin_X_black,1)
        time.sleep(0.1)
        i+=1


if __name__ == '__main__':
    main()

