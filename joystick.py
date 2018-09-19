#  -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
import sys
import time
import threading

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
            elif e.type == pygame.locals.JOYBALLMOTION:  # 8
                print('ball motion')
            elif e.type == pygame.locals.JOYHATMOTION:  # 9
                print('hat motion')
            elif e.type == pygame.locals.JOYBUTTONDOWN:  # 10
                print(str(e.button)+'番目のボタンが押された')
            elif e.type == pygame.locals.JOYBUTTONUP:  # 11
                print(str(e.button)+'番目のボタンが離された')

#ボタンは 0から11まで
#アナログボタンを押すと joyaixisモーションがアナログで動く
# 軸0 左アナログコントローラ左右(左が-1から1)
# 軸1 左アナログコントローラ上下(上が-1から下が1)
# 軸2 右アナログコントローラ左右(左が-1から下が1)
# 軸3 右アナログコントローラ上下(上が-1から下が1)
#プログラム(e.button) ジョイスティックの番号　位置
# 0 1ボタン
# 1 2ボタン
# 2 3ボタン
# 3 4ボタン 
# 4 5ボタン　左上トリガー
# 5 6ボタン  右上トリガー
# 6 7ボタン　左下トリガー
# 7 8ボタン　右下トリガー
# 8 9ボタン リセットボタン
# 9 9ボタン スタートボタン
# 10 左アナログボタン
# 11 右アナログボタンスイッチ 




if __name__ == '__main__':
    main()
