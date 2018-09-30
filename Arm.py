import math
import threading
import time
import RaspberryIo
import math
#  -*- coding: UTF-8 -*-

# //17
PALM_PINCH_IO = 17
# //18
WRIST_SNAP_IO = 18
# //22
ARM_ROTATE_IO = 22
# //23
ARM_ELBOW_IO = 23
# //24
ARM_SHOULDER_IO = 24
# //27
ARM_DIRECTION_IO = 27

# 長さのコンスタント
# 手首から軸まで
WRIST_LENGTH = 30
# 腕
ARM_LENGTH = 130
# 上腕
ARMLEVEL_LENGTH = 120
ARMLEVEL_LENGTH_ELBOW = 20
# 肩？（上腕の回転軸まで)
# 100で計算でもよいかも
SHOULDER_LENGTH = 99

# 腕の置いてある位置
# 左目の位置を原点として
#
ARM_LOCATION_X = 300
ARM_LOCATION_Y = 0
ARM_LOCATION_Z = 0


class Arm(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        print("初期化スタート")
        self.raspberry = RaspberryIo.RaspberryIo()
        self.rotateClockWise = True
        self.rotateCounterClockWise = False
        self.palmRoteateClockWise = True
        self.palmRoteateCounterClockWise = False
        self.palmPwmRate = 1250
        self.wristSnapRate = 1250
        self.armRotatePwmRate = 1250
        self.elbowRate = 500
        self.delta = 50
        self.shoulderRate = 500
        self.direction = 1250
        self.minPwmRate = 500
        self.maxPwmRate = 2000
        #p = threading.Thread()
        # p.start()

    def move(self, locationXyz):
        return "move x:" + str(locationXyz[0]) + " y: "+str(locationXyz[1])+" z: " + str(locationXyz[2])
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

    def setShoulder(self, value):
        self.shoulderRate = int(value)

    def setElbow(self, value):
        self.elbowRate = int(value)

    def setDirection(self, value):
        self.direction = int(value)

    def setWristSnap(self, value):
        self.wristSnapRate = int(value)

    def maxPwm(self, value):
        return value + self.delta < self.maxPwmRate

    def minPwm(self, value):
        return value - self.delta > self.minPwmRate

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
                if self.minPwm(self.palmPwmRate):
                    self.palmPwmRate -= self.delta
                self.raspberry.setOutput(PALM_PINCH_IO, self.palmPwmRate)
            # 手のひら時計回り
            if self.palmRoteateClockWise:
                if self.maxPwm(self.palmPwmRate):
                    self.palmPwmRate += self.delta
                self.raspberry.setOutput(PALM_PINCH_IO, self.palmPwmRate)
            # ローテート
            if self.rotateClockWise:
                if self.maxPwm(self.armRotatePwmRate):
                    self.armRotatePwmRate += self.delta
                self.raspberry.setOutput(ARM_ROTATE_IO, self.armRotatePwmRate)
            # 腕ローテート
            if self.rotateCounterClockWise:
                if self.minPwm(self.armRotatePwmRate):
                    self.armRotatePwmRate -= self.delta
                self.raspberry.setOutput(ARM_ROTATE_IO, self.armRotatePwmRate)
            # 手首
            self.raspberry.setOutput(WRIST_SNAP_IO, self.wristSnapRate)
            # 肘
            self.raspberry.setOutput(ARM_ELBOW_IO, self.elbowRate)
            # 肩
            self.raspberry.setOutput(ARM_SHOULDER_IO, self.shoulderRate)
            self.raspberry.setOutput(ARM_DIRECTION_IO, self.direction)

    # 腕の各角度を計算して予測位置(x,y,z)を計算する
    # x left to right
    # y height
    # z depth
    def calcPositionFromAngles(self, thetas):
        print("theta 1 " + str(thetas[0]) + "theta 2 " + str(thetas[1]) + "theta 3 " + str(
            thetas[2]) + "theta 4 " + str(thetas[3])+"theta 5" + str(thetas[4]) + "theta 6 " + str(thetas[5]))
        # 初期値(肩の高さ)
        shoulder_x = 0
        shoulder_y = 99
        shoulder_z = 0
        # 方から腕まで１（ジョイント部分）まで
        # theta5
        #
        elblow_x = 0
        elblow_y = ARMLEVEL_LENGTH * math.sin(thetas[4])
        elblow_z = ARMLEVEL_LENGTH * math.cos(thetas[4])

        # theta4
        # 方から腕のジョイント上の腕中心まで
        arm_start_x = 0
        arm_start_y = ARMLEVEL_LENGTH_ELBOW * math.sin(thetas[4] - thetas[3])
        arm_start_z = ARMLEVEL_LENGTH_ELBOW * math.cos(thetas[4] - thetas[3])

        #
        # theta
        # 腕付け根から腕先端まで
        #
        arm_end_x = 0
        arm_end_y = ARM_LENGTH * math.sin(thetas[3])
        arm_end_z = ARM_LENGTH * math.cos(thetas[3])

        # theta3
        # 手首
        wrist_x = 0
        wrist_y = - WRIST_LENGTH * math.sin(thetas[1])
        wrist_z = WRIST_LENGTH * math.cos(thetas[1])
        #位置計算
        hand_x = shoulder_x + elblow_x + arm_start_x + arm_end_x + wrist_x
        hand_y = shoulder_y + elblow_y + arm_start_y + arm_end_y + wrist_y
        hand_z = shoulder_z + elblow_z + arm_start_z + arm_end_z + wrist_z
        
        #回転させる
        # theta5だけ y 軸を中心に回転
        # math.cos(thetas[5]), 0 , math.sin(thetas[5])
        # 0,1,0
        # - math.sin(thetas[5]), 0 ,math.cos(thetas[5])
        #
        result_hand_x = math.cos(thetas[5]) * hand_x + 0 + math.sin(thetas[5])*hand_z
        result_hand_y = hand_y
        result_hand_z = - math.sin(thetas[5]) * hand_x + 0 + math.cos(thetas[5])*hand_z
        print(" hand x : " + str(result_hand_x) + " hand y : " +
              str(result_hand_y) + " hand z : " + str(result_hand_z))

