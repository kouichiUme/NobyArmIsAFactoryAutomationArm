import pigpio
import time


gpio_pin0 = 17
gpio_pin1 = 18


print("start pigpio");

pi = pigpio.pi()
pi.set_mode(gpio_pin0, pigpio.OUTPUT)
pi.set_mode(gpio_pin1, pigpio.OUTPUT)

pi.set_PWM_frequency(17,800)
pi.set_PWM_frequency(18,800)

pi.set_PWM_range(17,255)
pi.set_PWM_range(18,255)

pi.set_PWM_dutycycle(gpio_pin0,1)
pi.set_PWM_dutycycle(gpio_pin1,1)
#pi.hardware_PWM(gpio_pin1, 800, 100000)

time.sleep(5)
print("0 position")
pi.set_servo_pulsewidth(gpio_pin0,500)
pi.set_servo_pulsewidth(gpio_pin1,500)

time.sleep(5)
print("center")
pi.set_servo_pulsewidth(gpio_pin0,1500)
pi.set_servo_pulsewidth(gpio_pin1,1500)
time.sleep(5)

print("max position")
pi.set_servo_pulsewidth(gpio_pin0,2000)
pi.set_servo_pulsewidth(gpio_pin1,2000)

time.sleep(5)
print("finish servo")

pi.set_PWM_dutycycle(gpio_pin0,250)
pi.set_PWM_dutycycle(gpio_pin1,250)
#pi.hardware_PWM(gpio_pin1, 800, 100000)

time.sleep(5)
pi.set_PWM_dutycycle(gpio_pin0,0)
pi.set_PWM_dutycycle(gpio_pin1,0)
time.sleep(5)

pi.set_mode(gpio_pin0, pigpio.INPUT)
pi.set_mode(gpio_pin1, pigpio.INPUT)
pi.stop()
