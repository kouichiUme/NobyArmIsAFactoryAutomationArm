#  -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
import sys
import math
import time
import threading

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
                roundArm(x,y)
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
        hand_Grasp()
    elif button == RIGHT_UP_TRIGGER:
        hand_Grasp()
    elif button == LEFT_DOWN_TRIGGER:
        hand_Grasp()
    elif button == RIGHT_DOWN_TRIGGER:
        hand_Grasp()


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
        hand_release()
    elif button == RIGHT_UP_TRIGGER:
        hand_release()
    elif button == LEFT_DOWN_TRIGGER:
        hand_release()
    elif button == RIGHT_DOWN_TRIGGER:
        hand_release()

#


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
# 動き
#


def roundArm(armX, armY):
    print(" " + str(armX) + " " + str(armY))
# x,yから向きを計算して
# x^2 + y~2から 腕の伸び具合を計算します
    x2 = armX*armX
    y2 = armY*armY
    v = math.sqrt(x2+y2)
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
        print(" i : " + str(abs(i/vmax)) + " theta : " + str(theta1))

# 向き
# acos(x/abs(x))
#
# x*x + y*Y /abs(max(x)^2 + max(y)^2)
# maxx = 1 , maxy = 1

# ロボットアーム向き
# 腕の回転角度をもらってそこに移動する
def robotArmDirection(theta):
    print("theta :" + str(theta))
# ここでロボットアーム側PWMに変換する


#
# ロボットアームの肩
#
def robotArmSholder(theta):
    print("sholder theta :" + str(theta))
# ここでロボットアーム側PWMに変換する


#
# ロボットアーム腕部分
#
def robotArmElbow(theta):
    print("elbow theta :" + str(theta))
# ここでロボットアーム側PWMに変換する

# ロボットアーム腕の回転


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
