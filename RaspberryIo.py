#  -*- coding: UTF-8 -*-
#import pigpio
import time

#ラズベリーパイ上で動くモジュール
class RaspberryIo :
    def __init__(self):
 #       self.pi = pigpio.pi()
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