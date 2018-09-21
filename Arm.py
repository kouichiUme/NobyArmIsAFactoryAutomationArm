import math
#  -*- coding: UTF-8 -*-
class Arm:
    def __init__(self):
        print("初期化スタート")

    def move(self,x,y,z):
        print("move x:" + str(x) +"y: "+str(y)+"z: "+ str(z)) 

        #動きxに対してそれぞれ計算する
        # x方向 theta = arctangent(x)
        # theta1 = math.asin(x)
        # if( math.abs(y - math.cos(theta1)) < 0.000001)
        #   else theta1 = math.pi - theta1 
        #   unitActiveRadian = rangeTheta / (maxPwmValue - minPwmValue )  稼働領域
        #  deltaPwmDutyRate = ( maxPwmValue - minPwmValue ) * theta1 /  unitActiveRadian 
        # pwmDutyRate = 500(minPwmValue) + deltaPwmDutyRate 
        # axis1
        # axis1
        # axis1
        return "move x:" + str(x) +" y: "+str(y)+" z: "+ str(z)

    def calc(self):
        print("calc start")

    #腕軸部分時計回り回転
    def startRotateClockWise(self):
        print("start rotate arm")
        
    def stopRotateClockWise(self):
        print("stop rotate arm")

    #腕軸部分時計回り回転
    def startRotateCounterClockWise(self):
        print("start counter rotate arm")
        
    def stopRotateCounterClockWise(self):
        print("stop counter  rotate arm")


    #手首
    def startPalmRoteteClockWise(self):
        print("start palm rotate clock")
        
    def stopPalmRoteteClockWise(self):
        print("stop palm rotate clock")

    #腕軸部分時計回り回転
    def startPalmtRotateCounterClockWise(self):
        print("start palm counter rotate ")
        
    def stopPalmRotateCounterClockWise(self):
        print("stop palm counter  rotate ")



