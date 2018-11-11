#  -*- coding: UTF-8 -*-
#import pigpio
import time

#ラズベリーパイ上で動くモジュール
class RaspberryIo :
    def __init__(self):
#       self.pi = pigpio.pi()
#        pi = pigpio.pi()
#       pi.set_mode(gpio_pin0, pigpio.OUTPUT)
#        pi.set_mode(gpio_pin1, pigpio.OUTPUT)

        #50Hz Frequency(20ms)
        # dutyRange(1ms 5ms)
        #5%  25%がレンジ
        #pi.set_PWM_frequency(17,800)
 #       pi.set_PWM_frequency(18,800)
 #       pi.set_PWM_range(17,255)
 #       pi.set_PWM_range(18,255)
        return

    def setIoMode(self,io,mode):
         #self.pi.set_mode(io, mode)
         return


    def setPwmFrequency(self,io,frequency):
    #       self.pi.set_PWM_frequency(io,frequency)
        return

    def setPwmOutput(self,io,value):
    #self.pi.set_servo_pulsewidth(io,value)
        return

    #output port io
    #value O or 1
    def writeOutput(self,io,value):
        print("io port : " + str(io) +"  value :" + str(value))

        #      self.pi.write(io,value)
        return