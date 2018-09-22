import math
import threading
import time
#  -*- coding: UTF-8 -*-


class Arm(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        print("初期化スタート")
        self.rotateClockWise = True
        self.rotateCounterClockWise = False
        self.palmRoteateClockWise = True
        self.palmRoteateCounterClockWise = False
        self.palmPwmRate = 0
        self.armRotatePwmRate = 0
        self.delta = 50
        #p = threading.Thread()
        # p.start()

    def move(self, x, y, z):
        print("move x:" + str(x) + "y: "+str(y)+"z: " + str(z))

        # 動きxに対してそれぞれ計算する
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
        return "move x:" + str(x) + " y: "+str(y)+" z: " + str(z)

    def calc(self):
        print("calc start")

    # 腕軸部分時計回り回転
    def startRotateClockWise(self):
        self.rotateClockWise = True
        print("start rotate arm")

    def stopRotateClockWise(self):
        self.rotateClockWise = False
        print("stop rotate arm")

    # 腕軸部分時計回り回転
    def startRotateCounterClockWise(self):
        self.rotateCounterClockWise = True
        print("start counter rotate arm")

    def stopRotateCounterClockWise(self):
        self.rotateCounterClockWise = False
        print("stop counter  rotate arm")

    # 手首
    #

    def startPalmRoteteClockWise(self):
        self.palmRoteateClockWise = True
        #self.thetaOfPlam += deltaTheta
        print("start palm rotate clock")

    def stopPalmRoteteClockWise(self):
        self.palmRoteateClockWise = False
        print("stop palm rotate clock")

    # 腕軸部分時計回り回転
    def startPalmtRotateCounterClockWise(self):
        self.palmRoteateCounterClockWise = True
        print("start palm counter rotate ")

    def stopPalmRotateCounterClockWise(self):
        self.palmRoteateCounterClockWise = False
        print("stop palm counter  rotate ")

    # ボタン押されているもののpwmパラメータ値を上昇させる

    def run(self):
        time.sleep(0.1)
        count = 0
        while True:
            count += 1
            if count % 10 == 0:
                print("palmPwm " + str(self.palmPwmRate))
                print("armPwm " + str(self.armRotatePwmRate))
            time.sleep(0.1)
            # 手のひら反対時計回り
            if self.palmRoteateCounterClockWise:
                self.palmPwmRate -= self.delta
            # 手のひら時計回り
            if self.palmRoteateClockWise:
                self.palmPwmRate += self.delta
            # ローテート
            if self.rotateClockWise:
                self.armRotatePwmRate += self.delta
            # ローテート
            if self.rotateCounterClockWise:
                self.armRotatePwmRate -= self.delta
