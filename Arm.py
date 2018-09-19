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

        