import time
import math

#計算用モジュール
# 現在位置と対象までの計算問題はできるので、解く。
# 距離、腕の動かし方、動かし方はできたらプランニングできたらより良い
# あと、映っているものが何かを学習させるのがいいかも
# 映っているものと、目的のものがあるかないかのマッチ
class Distance :
    def __init__(self):
 #       self.pi = pigpio.pi()
        # 座標軸上の100,100,100に腕があるとします。
        self.armPosition = [100,100,100]
        return
    #
    # 画面内のXYと深度から0をベースとして計算
    #
    def calcImageDistance(self,inImageLocation):
        print("calc from distance in image")

    #
    # 
    def calcDistanceBetween(self,targetToGrab):
        print("x: " + str(self.armPosition[0]) +" y:" + str( self.armPosition[1]) + " z:" + str(self.armPosition[2]) )
        print("target x: " + str(targetToGrab[0]) +" target  y:" + str( targetToGrab[1]) + " target  z:" + str(targetToGrab[2]) )
        
        print("distance program")
        return


    #腕の可動域内か計算する
    #
    def isInTheReach(self,targetToGrab):



    # 腕の可動域外の場合は、モーターで移動する分を計算する。
    # X,Y,Z
    # 腕分だけ少し手前で止まるため
    def calcMoveDistance(self,targetToGrab):


