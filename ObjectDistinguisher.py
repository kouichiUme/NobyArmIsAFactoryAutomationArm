# 映っているものと、目的のものがあるかないかのマッチ
#もののデータか(；´Д`A学習させる画像とか
#ナス、キュウリ、トマトぐらいか？
#とりあえず、紫、みどり、赤のものでいいか( ＾∀＾)
import Distance


class ObjectDistinguisher :
    def __init__(self):
#self.pi = pigpio.pi()
        return

#画面を動かして探す
    def detect(self,objectName):
        print("distance program")
        #カメラを動かす

        return


#画面からオブジェクト切り出したものが何かをチェックする
    def checkObject(self,objectImage):
        #学習結果から
        print("objectImageを教科学習レイヤーに食わせて何かを判断します")
        # objectImage

#オブジェクトのテンプレートがあればそこから画像チェックをする
    def detectObjectByTemplate(self,objectName):
        #テンプレートサーチ
        print("template search ")

#オブジェクトとの距離を計算する
    def meatureDistance(self,objectImage):
        #距離計算をする
        print("イメージから距離計算をする")
        #例えば100cmとする本来なら画像から距離を計算する
        # image1とimage2から視差を計算する

        fromObject = [100,200,200]
        # 距離計算する
        dist= Distance.Distance()
        dist.calcDistanceBetween(fromObject)
    