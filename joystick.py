#  -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
import sys
sys.path.append(".")
import math
import time
import threading
import Arm

arm = Arm.Arm()
arm.setDaemon(True)
arm.start()

# ボタンは 0から11まで
# アナログボタンを押すと joyaixisモーションがアナログで動く
# 軸0 左アナログコントローラ左右(左が-1から1)
# 軸1 左アナログコントローラ上下(上が-1から下が1)
# 軸2 右アナログコントローラ左右(左が-1から下が1)
# 軸3 右アナログコントローラ上下(上が-1から下が1)
# プログラム(e.button) ジョイスティックの番号　位置
# 0 1ボタン
RIGHT_ONE_BUTTON = 0
# if e.button == RIGHT_ONEBUTTON :
#    print("1 button pushed");
# 1 2ボタン
RIGHT_TWO_BUTTON = 1
# 2 3ボタン
RIGHT_THREE_BUTTON = 2
# 3 4ボタン
RIGHT_FOUR_BUTTON = 3
# 4 5ボタン　左上トリガー
LEFT_UP_TRIGGER = 4
# 5 6ボタン  右上トリガー
RIGHT_UP_TRIGGER = 5
# 6 7ボタン　左下トリガー
LEFT_DOWN_TRIGGER = 6
# 7 8ボタン　右下トリガー
RIGHT_DOWN_TRIGGER = 7
# 8 9ボタン リセットボタン
RESET_BUTTON = 8
# 9 9ボタン スタートボタン
START_BUTTON = 9
# 10 左アナログボタン
LEFT_ANALOG_BUTTON = 10
# 11 右アナログボタンスイッチ
RIGHT_ANALOG_BUTTON = 11

pygame.joystick.init()


try:
    j = pygame.joystick.Joystick(0)
    j.init()
except pygame.error:
    print('ジョイスティックを差し込め')


def main():
    pygame.init()


    while True:

        for e in pygame.event.get():  # イベントチェック
            if e.type == QUIT:  # 終了が押された？
                return
            if (e.type == KEYDOWN and
                    e.key == K_ESCAPE):  # ESCが押された？
                return
            # Joystick関連のイベントチェック
            if e.type == pygame.locals.JOYAXISMOTION:  # 7
                x, y = j.get_axis(0), j.get_axis(1)
                z, t = j.get_axis(2), j.get_axis(3)
                print('x and y : ' + str(x) + ' , ' + str(y))
                print('z and t : ' + str(z) + ' , ' + str(t))
                v,theta1 = roundArm(x,y)
                v2,theta2 =  roundArm(z, t)
                robotArmDirection(theta1)
                robotArmShoulder(v)
                robotArmWristSnap(theta2)
                robotArmElbow(v2)
            elif e.type == pygame.locals.JOYBALLMOTION:  # 8
                print('ball motion')
            elif e.type == pygame.locals.JOYHATMOTION:  # 9
                print('hat motion')
            elif e.type == pygame.locals.JOYBUTTONDOWN:  # 10
                pressedButton(e.button)
                print(str(e.button)+'番目のボタンが押された')
            elif e.type == pygame.locals.JOYBUTTONUP:  # 11
                releasedButton(e.button)
                print(str(e.button)+'番目のボタンが離された')

#
# ボタン押したら特定の方向に進む
#


def pressedButton(button):
    print("button " + str(button) + " is pressed ")
    if button == RIGHT_ONE_BUTTON:
        arm_X_Move()
    elif button == RIGHT_TWO_BUTTON:
        arm_Y_MOVE()
    elif button == RIGHT_THREE_BUTTON:
        arm_Z_MOVE()
    elif button == RIGHT_FOUR_BUTTON:
        arm_T_MOVE()
    elif button == LEFT_UP_TRIGGER:
        robotArmRotateClockWiseStart()
    elif button == RIGHT_UP_TRIGGER:
        robotArmPalmPinchClockWiseStart()
    elif button == LEFT_DOWN_TRIGGER:
        robotArmRotateCounterClockWiseStart()
    elif button == RIGHT_DOWN_TRIGGER:
        robotArmPalmPinchCounterClockWiseStart()


# comment
# ボタン離したときには停止
#
#
def releasedButton(button):
    print("button " + str(button) + " is released ")
    if button == RIGHT_ONE_BUTTON:
        arm_X_stop()
    elif button == RIGHT_TWO_BUTTON:
        arm_Y_STOP()
    elif button == RIGHT_THREE_BUTTON:
        arm_Z_STOP()
    elif button == RIGHT_FOUR_BUTTON:
        arm_T_STOP()
    elif button == LEFT_UP_TRIGGER:
        robotArmRotateClockWiseStop()
    elif button == RIGHT_UP_TRIGGER:
        robotArmPalmPinchClockWiseStop()
    elif button == LEFT_DOWN_TRIGGER:
        robotArmRotateCounterClockWiseStop()
    elif button == RIGHT_DOWN_TRIGGER:
        robotArmPalmPinchCounterClockWiseStop()

#
# 腕の軸部分
# 時計回りに回るように thetaを増やすメソットを開始する
#
def robotArmRotateClockWiseStart():
    print("start rotate clockwise")
    time.sleep(0.1)
    arm.startRotateClockWise()
    #theta += 10
    #
    #robotArmRotate(theta)
    return
#
# 停止する
def robotArmRotateClockWiseStop():
    print("stop rotate clockwise")
    arm.stopRotateClockWise()
    #stopRotate()
    return

#腕軸部分の時計回り回転
# theta を減らすような内部メソッドを呼び出す
def robotArmRotateCounterClockWiseStart():
    print("start rotate counter clockwise")
    arm.startRotateCounterClockWise()
    return

def robotArmRotateCounterClockWiseStop():
    print("stop rotate counter clockwise")
    arm.stopRotateCounterClockWise()
    return



#手首半時計回りに回す開始
def robotArmPalmPinchClockWiseStart():
    print("startrotate palm clockwise")
    arm.startPalmRoteteClockWise()
    return

#手首半時計回りに回す停止
def robotArmPalmPinchClockWiseStop():
    print("stop rotate palm clockwise")
    arm.stopPalmRoteteClockWise()
    return

#手首半時計回りに回す
def robotArmPalmPinchCounterClockWiseStart():
    print("startrotate palm counter clockwise")
    arm.startPalmtRotateCounterClockWise()
    return

#手首半時計回りに回す
def robotArmPalmPinchCounterClockWiseStop():
    print("stop rotate palm counter clockwise")
    arm.stopPalmRotateCounterClockWise()
    return





def arm_X_Move():
    print("x move")
#


def arm_X_stop():
    print("x stop")

#


def arm_Y_MOVE():
    print("y move")


def arm_Y_STOP():
    print("y move")
#


def arm_Z_MOVE():
    print("Z move")


def arm_Z_STOP():
    print("Z move")


def arm_T_MOVE():
    print("T move")


def arm_T_STOP():
    print("T move")

#


def hand_Grasp():
    print("grasp")


def hand_release():
    print("release")

#
# アナログジョイスティック
#
# 角度と伸び具合をあらわすヴェクトル絶対値を返す
#
def roundArm(armX, armY):
    print(" " + str(armX) + " " + str(armY))
# x,yから向きを計算して
# x^2 + y~2から 腕の伸び具合を計算します
    x2 = armX*armX
    y2 = armY*armY
    v = math.sqrt(x2+y2)
    v0 = v
    theta1 = 0
    # 0 < math.acos < math.pi
    # math.asin < 0
    #
    if abs(v) > 0.0000001:
        theta1 = math.acos(armX/v)
    # - math.pi /2 < math.asin < math.pi /2
        theta2 = math.asin(armY/v)
        theta_t = 0
        if armX < 0 and armY < 0:
            theta1 = - theta1
            theta2 = -( math.pi) - theta2
            #math.pi/4 より大
            if abs(armX) < abs(armY) :
                theta_t =  math.pi/2 - theta1
            else:
                theta_t = -math.pi - theta1
        elif armX < 0 and armY > 0:
            theta1 = theta1
            theta2 = math.pi - theta2
            if abs(armX) < abs(armY) :
                theta_t = theta1 - math.pi /2
            else:
                theta_t = math.pi - theta1
        elif armX > 0 and armY < 0: 
            theta1 = -theta1
            theta2 = theta2
            if abs(armX) < abs(armY) :
                theta_t = -math.pi/2 - theta1
            else:
                theta_t = - theta1
        elif armX > 0 and armY > 0:
            theta1 = theta1
            theta2 = theta2
            if abs(armX) < abs(armY) :
                theta_t = math.pi/2 - theta1
            else:
                theta_t = theta1
        elif armX > 0 :
            theta1 = 0
            theta2 = 0
            theta_t = 0
        elif armX < 0:
            # 2 math.piのとき
            theta2 =  math.pi
            theta1 =  math.pi
            theta_t =0
        elif armY > 0:
            theta2 =  math.pi/2
            theta1 =  math.pi/2
            theta_t = 0
        elif armY < 0:
            theta2 = - math.pi/2
            theta1 = - math.pi/2
            theta_t = 0
        print("theta1 " + str(theta1) + " theta2:" + str(theta2))
        i = math.sin(theta1)*armY + math.cos(theta1)*armX
        vmax = math.sqrt(1 + math.tan(theta_t)*math.tan(theta_t))
        v0 = abs(i/vmax)
        print(" i : " + str(abs(i/vmax)) + " theta : " + str(theta1))
    return v0,theta1

# 向き
# acos(x/abs(x))
#
# x*x + y*Y /abs(max(x)^2 + max(y)^2)
# maxx = 1 , maxy = 1
minPwmValue = 500
maxPwmValue = 2000
rangePwm = maxPwmValue - minPwmValue
centerPwmValue = (maxPwmValue + minPwmValue) /2
# ロボットアーム向き
# 腕の回転角度をもらってそこに移動する
# - math.pi < theta < math.pi
def robotArmDirection(theta):
    print("theta :" + str(theta))
    degree = theta/(2*math.pi)
    pwmRate = rangePwm * degree + centerPwmValue
    print("pwm rate  : " + str(pwmRate))
# ここでロボットアーム側PWMに変換する
    

#
# ロボットアームの肩
# 肩一番下のサーボの開閉
# デフォルトは0の状態
# 0 < v < 1
minShoulderPwmValue = 500
maxShoulderPwmValue = 2000
centerShoulderPwmValue = (maxShoulderPwmValue + minShoulderPwmValue) /2
def calcRangePwm(x,y):
    return y - x

randgeShoulderPwmValue = calcRangePwm(minShoulderPwmValue,maxShoulderPwmValue)

def robotArmShoulder(theta):
    print("shoulder theta :" + str(theta))
    randgeShoulderPwmValue = calcRangePwm(minShoulderPwmValue,maxShoulderPwmValue)
    shoulderPwmRate = randgeShoulderPwmValue * theta
    if theta < 0.000001 :
         shoulderPwmRate = 0 #free
    else :
        shoulderPwmRate += minShoulderPwmValue
    print("shoulder pwm :" + str(shoulderPwmRate))
    shoulderPwmRate = maxShoulderPwmValue - shoulderPwmRate
    arm.setShoulder(shoulderPwmRate)
# ここでロボットアーム側PWMに変換する
    


#
# ロボットアーム腕部分
# 肩とほぼ同じ
minElbowPwmValue = 500
maxElbowPwmValue = 2000
def robotArmElbow(theta):
    print("elbow theta :" + str(theta))
    randgeElbowPwmValue = calcRangePwm(minElbowPwmValue,maxElbowPwmValue)
# ここでロボットアーム側PWMに変換する
    elbowPwmRate = randgeElbowPwmValue * theta
    if theta < 0.000001 :
        elbowPwmRate = 0
    else:
        elbowPwmRate += minElbowPwmValue
    print("elbow pwm :" + str(elbowPwmRate))
    arm.setShoulder(elbowPwmRate)


# ロボットアーム腕の回転
# 
def robotArmRotate(theta):
    print("rotate theta :" + str(theta))
# ここでロボットアーム側PWMに変換する


# ロボットの手首スナップ（上下）
def robotArmWristSnap(theta):
    print("Snap :" + str(theta))
# ここでロボットアーム側PWMに変換する

# ロボットの手でつまむ部分の回転


def robotArmPalmPinch(theta):
    print("PalmPinch :" + str(theta))
# ここでロボットアーム側PWMに変換する


if __name__ == '__main__':
    main()
