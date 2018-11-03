
# -*- coding: utf-8 -*-
#import pigpio
import time
import threading
import time
import RaspberryIo
import math

# X is black
# X_ is orange
# Y is brown
# Y_ is yellow
# 2 phase
# gear radiusから 計算をして移動距離を計算する。
# parameter R ロボットに固有
#
# 移動距離 distance = omega*R
# omega = distance / R
# unitOfRotation  = 3.75
# stepNum = omega / 1 unitOfRotation 3.75
#
#
# steppingmotorの内部状態を保持する
# 4相あるので、次どこからすすめるのか
# スレッドにするのと、ポートを初期化時に渡せるようにしたい
# 1 step 3.75 degree
# 2 PI round 96 step
#       1               2
# X     on  on off off  on on off
# X_    off on on  off  off on on
# Y     off off on on   off off on
# Y_    on off off on   on off off
# clockwise

# X direction

gpio_pin_X_orange = 12
gpio_pin_X_yellow = 16
gpio_pin_X_brown = 20
gpio_pin_X_black = 21

# Y direction (height)

gpio_pin_Y_orange = 15
gpio_pin_Y_yellow = 25
gpio_pin_Y_brown = 8
gpio_pin_Y_black = 7

# Z direction (height)

gpio_pin_Z_orange = 2
gpio_pin_Z_yellow = 3
gpio_pin_Z_brown = 4
gpio_pin_Z_black = 14
#pi = pigpio.pi()

# 半径
# ioportのポート番号


class SteppedMotor(threading.Thread):
    def __init__(self, r, portNumX, portNumX_, portNumY, portNumY_):
        threading.Thread.__init__(self)
        self.radius = r
        self.portNumX = portNumX
        self.portNumX_ = portNumX_
        self.portNumY = portNumY
        self.portNumY_ = portNumY_
        self.unitOfRotation = 3.75 #degree
        self.raspberryIo = RaspberryIo.RaspberryIo()
        # モータの状態を0,1,2,3で表現する
        # 途中から回転を始める時のためのもの
        self.motorState = 0
        # X     on  on off off  on on off
        # X_    off on on  off  off on on
        # Y     off off on on   off off on
        # Y_    on off off on   on off off
        # state table  
        self.statePortTable = [[self.portNumX,self.portNumY],
        [self.portNumX_,self.portNumY_],[self.portNumX,self.portNumY],[self.portNumX_,self.portNumY_]]
        self.stateValueTable = [[1,0],[1,0],[0,1],[0,1]]

    def move(self, distanceX):
        print("distance X : " + str(distanceX))
        moveOmega = distanceX / self.radius
        # radian
        stepNumber = 180 * moveOmega / self.unitOfRotation
        print("step number : " + str(stepNumber))
        self.stepped(stepNumber)
        return
 
    def stepped(self,stepNumber):
        #for i : i < stepNumber :
            print( " step " + str(stepNumber))
            print( " state  " + str(self.motorState))
            step = math.floor(stepNumber)
            for i in range(step):
                print("step i :" + str(i))
                print("state : " + str(self.motorState))
                #X X_ Y Y_に出力
                # portState[i]
                self.write()
                #状態を変える
            return
    #出力する port番号は初期化済みだから stateの状態で出力するペアを決める
    def write(self):
        ports = self.getOutputNextPort()
        values = self.getOutputNextValue()
        #X
        print("write output port : " + str(ports[0])+ " value : " + str(values[0]))
        self.raspberryIo.writeOutput(ports[0],values[0])
        #X_
        print("write output port : " + str(ports[1])+ " value : " + str(values[1]))
        self.raspberryIo.writeOutput(ports[1],values[1])
        self.motorState += 1
        self.motorState %= 4
        return
    def getOutputNextPort(self):
        
        ports =  self.statePortTable[self.motorState]
        return ports

    def getOutputNextValue(self):
        values =  self.stateValueTable[self.motorState]
        return values

def main():
    print("start pigpio")
    #pi.set_mode(gpio_pin_X_orange, pigpio.OUTPUT)
    #pi.set_mode(gpio_pin_X_yellow, pigpio.OUTPUT)
    #pi.set_mode(gpio_pin_X_brown, pigpio.OUTPUT)
    #pi.set_mode(gpio_pin_X_black, pigpio.OUTPUT)
    time.sleep(5)
    startCWRotate(True)
    startYCWRotate(True)
    startZCWRotate(True)
    startCCWRotate(True)


def startCWRotate(startStop):
    # X is black
    # X_ is orange
    # Y is brown
    # Y_ is yellow
    # 2 phase
    # 1 step 3.75 degree
    #       1               2
    # X     on  on off off  on on off
    # X_    off on on  off  off on on
    # Y     off off on on   off off on
    # Y_    on off off on   on off off
    # clockwise
    i = 0
    while startStop and i < 30:
        #pi.write(gpio_pin_X_black, 1)
        #pi.write(gpio_pin_X_yellow, 0)
        time.sleep(0.1)

        #pi.write(gpio_pin_X_orange, 1)
        time.sleep(0.1)
        #pi.write(gpio_pin_X_black, 0)
        time.sleep(0.1)
        #pi.write(gpio_pin_X_brown, 1)
        time.sleep(0.1)
        #pi.write(gpio_pin_X_orange, 0)
        time.sleep(0.1)
        #pi.write(gpio_pin_X_yellow, 1)
        time.sleep(0.1)
        #pi.write(gpio_pin_X_brown, 0)
        time.sleep(0.1)
        i += 1
#


def startYCWRotate(startStop):
    # X is black
    # X_ is orange
    # Y is brown
    # Y_ is yellow
    # 2 phase
    # 1 step 3.75 degree
    # 2 PI round 96 step
    #       1               2
    # X     on  on off off  on on off
    # X_    off on on  off  off on on
    # Y     off off on on   off off on
    # Y_    on off off on   on off off
    # clockwise
    i = 0
    while startStop and i < 30:
        #pi.write(gpio_pin_Y_black, 1)
        #pi.write(gpio_pin_Y_yellow, 0)
        time.sleep(0.1)

        #pi.write(gpio_pin_Y_orange, 1)
        time.sleep(0.1)
        #pi.write(gpio_pin_Y_black, 0)
        time.sleep(0.1)
        #pi.write(gpio_pin_Y_brown, 1)
        time.sleep(0.1)
        #pi.write(gpio_pin_Y_orange, 0)
        time.sleep(0.1)
        #pi.write(gpio_pin_Y_yellow, 1)
        time.sleep(0.1)
        #pi.write(gpio_pin_Y_brown, 0)
        time.sleep(0.1)
        i += 1
#


def startZCWRotate(startStop):
    # X is black
    # X_ is orange
    # Y is brown
    # Y_ is yellow
    # 2 phase
    # 1 step 3.75 degree
    #       1               2
    # X     on  on off off  on on off
    # X_    off on on  off  off on on
    # Y     off off on on   off off on
    # Y_    on off off on   on off off
    # clockwise
    i = 0
    while startStop and i < 30:
     #   pi.write(gpio_pin_Z_black, 1)
     #   pi.write(gpio_pin_Z_yellow, 0)
        time.sleep(0.1)

 #       pi.write(gpio_pin_Z_orange, 1)
        time.sleep(0.1)
 #       pi.write(gpio_pin_Z_black, 0)
        time.sleep(0.1)
   #     pi.write(gpio_pin_Z_brown, 1)
        time.sleep(0.1)
  #      pi.write(gpio_pin_Z_orange, 0)
        time.sleep(0.1)
    #    pi.write(gpio_pin_Z_yellow, 1)
        time.sleep(0.1)
    #    pi.write(gpio_pin_Z_brown, 0)
        time.sleep(0.1)
        i += 1
#


def startCCWRotate(startStop):
    # counter clock wise
    i = 0
    while startStop and i < 30:
        #pi.write(gpio_pin_X_brown, 0)
        time.sleep(0.1)
      #  pi.write(gpio_pin_X_yellow, 1)
        time.sleep(0.1)
       # pi.write(gpio_pin_X_orange, 0)
        time.sleep(0.1)
        #pi.write(gpio_pin_X_brown, 1)
        time.sleep(0.1)
    #    pi.write(gpio_pin_X_black, 0)
        time.sleep(0.1)
     #   pi.write(gpio_pin_X_orange, 1)
        time.sleep(0.1)
      #  pi.write(gpio_pin_X_yellow, 0)
        time.sleep(0.1)
       # pi.write(gpio_pin_X_black, 1)
        time.sleep(0.1)
        i += 1


if __name__ == '__main__':
    main()
