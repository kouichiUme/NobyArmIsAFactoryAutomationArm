#  -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
import time

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
                print('x and y : ' + str(x) + ' , ' + str(y))
            elif e.type == pygame.locals.JOYBALLMOTION:  # 8
                print('ball motion')
            elif e.type == pygame.locals.JOYHATMOTION:  # 9
                print('hat motion')
            elif e.type == pygame.locals.JOYBUTTONDOWN:  # 10
                print(str(e.button)+'番目のボタンが押された')
            elif e.type == pygame.locals.JOYBUTTONUP:  # 11
                print(str(e.button)+'番目のボタンが離された')


if __name__ == '__main__':
    main()
