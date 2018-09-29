
# -*- coding: utf-8 -*-
import pigpio
import time


gpio_pin_orange = 12
gpio_pin_yellow = 16
gpio_pin_brown = 20
gpio_pin_black = 21


print("start pigpio")

pi = pigpio.pi()
pi.set_mode(gpio_pin_orange, pigpio.OUTPUT)
pi.set_mode(gpio_pin_yellow, pigpio.OUTPUT)
pi.set_mode(gpio_pin_brown, pigpio.OUTPUT)
pi.set_mode(gpio_pin_black, pigpio.OUTPUT)
time.sleep(5)

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
while True:
    pi.write(gpio_pin_black, 1)
    pi.write(gpio_pin_yellow, 0)
    pi.write(gpio_pin_orange, 1)

    pi.write(gpio_pin_black, 0)
    pi.write(gpio_pin_brown, 1)

    pi.write(gpio_pin_orange, 0)
    pi.write(gpio_pin_yellow, 1)
    pi.write(gpio_pin_brown, 0)


# counter clock wise
#    pi.write(gpio_pin_black,1)
#    pi.write(gpio_pin_yellow,0)
#    pi.write(gpio_pin_orange,1)

# pi.write(gpio_pin_black,0)
# pi.write(gpio_pin_brown,1)

# pi.write(gpio_pin_orange,0)
# pi.write(gpio_pin_yellow,1)
# pi.write(gpio_pin_brown,0)
