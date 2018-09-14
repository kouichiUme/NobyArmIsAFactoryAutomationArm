import pigpio
import time


gpio_pin0 = 17
gpio_pin1 = 18


print("start pigpio");

pi = pigpio.pi()
pi.set_mode(gpio_pin0, pigpio.OUTPUT)
pi.set_mode(gpio_pin1, pigpio.OUTPUT)

pi.set_PWM_range(17,800)
pi.set_PWM_dutycycle(gpio_pin0,255)
#pi.hardware_PWM(gpio_pin1, 800, 100000)

time.sleep(5)
pi.set_PWM_dutycycle(gpio_pin0,0)

pi.set_mode(gpio_pin0, pigpio.INPUT)
#pi.set_mode(gpio_pin1, pigpio.INPUT)
pi.stop()
