import Distance
import numpy
#
#左目の位置が原点
LEFT_EYE_LOCATION_X=0
LEFT_EYE_LOCATION_Y=0
LEFT_EYE_LOCATION_Z=0

#左目と右目の間の距離
LENGTH_BETWEEN_LEFTEYE_AND_RIGHTEYE = 100

class NobyEyes:
    def __init__(self):
        print("Mノビィの目 初期化")
    
#オブジェクトとの距離を計算する
#
    def meatureDistance(self):
        #距離計算をする
        print("イメージから距離計算をする")
        # 例えば100cmとする本来なら画像から距離を計算する
        # distance_x =  
        # image1とimage2から視差を計算する
        # 左目を軸として左目の位置からのイメージの位置を計算する
        # 目の間の距離
        b = LENGTH_BETWEEN_LEFTEYE_AND_RIGHTEYE
        #左目から見た距離[mm](多分実測してカメラの焦点距離とか視野角から計算する必要がある)
        x_left = 100
        x_right = 8
        y_left = 100
        #y_right = 100
        z = b / ( x_left - x_right )
        x = x_left * z
        y = y_left * z
        fromLeftEyeDistance = [x,y,z]
        return fromLeftEyeDistance
