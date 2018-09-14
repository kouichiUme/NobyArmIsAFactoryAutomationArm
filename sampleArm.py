import pigpio
import time


gpio_pin0 = 18
gpio_pin1 = 19


print("start pigpio");

pi = pigpio.pi()
pi.set_mode(gpio_pin0, pigpio.OUTPUT)
pi.set_mode(gpio_pin1, pigpio.OUTPUT)

pi.hardware_PWM(gpio_pin0,800,255)
# GPIO19: 8Hz、duty比0.1
pi.hardware_PWM(gpio_pin1, 800, 100000)

time.sleep(5)

pi.set_mode(gpio_pin0, pigpio.INPUT)
pi.set_mode(gpio_pin1, pigpio.INPUT)
pi.stop()
