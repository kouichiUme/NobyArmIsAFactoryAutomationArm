import RaspberryIo

# 頭・首まわり
# port 2,3,4で storm32を回す
NOBY_GIMBAL_PORT_ROLL_IOPORT=2
NOBY_GIMBAL_PORT_PITCH_IOPORT=3
NOBY_GIMBAL_PORT_YAW_IOPORT=4

#
class NobyNeckMoverGimbalStorm:
    def __init__(self):
        print("NobyNeckMoverGimbalStorm start")
        self.raspberry = RaspberryIo.RaspberryIo()

        # まとめて向きを変える場合
        # roll , pitch ,yaw

    def moveRotate(self, roll, pitch, yaw):
        print("roll : " + str(roll) + " pitch: " + str(pitch) + " yaw :" + str(yaw))
        #
        #
        #

    #向きから x y z 方向から 回転計算をする
    #現在の角度が必要かも
    def direction(self, x, y, z):
        print("x : " + str(x) + " y: " + str(y) + " z :" + str(z))

