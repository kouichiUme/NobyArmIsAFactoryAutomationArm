import pigpio
import time


gpio_pin0 = 18
gpio_pin1 = 19



pi = pigpio.pi()
pi.set_mode(gpio_pin0, pigpio.OUTPUT)
pi.set_mode(gpio_pin1, pigpio.OUTPUT)

pi.pwmWrite()
# GPIO19: 8Hz、duty比0.1
pi.hardware_PWM(gpio_pin1, 8, 100000)

time.sleep(5)

pi.set_mode(gpio_pin0, pigpio.INPUT)
pi.set_mode(gpio_pin1, pigpio.INPUT)
pi.stop()