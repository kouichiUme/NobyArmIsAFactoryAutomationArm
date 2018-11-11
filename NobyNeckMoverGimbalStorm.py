import RaspberryIo

# 頭・首まわり
# port 13,19,26で storm32を回す
# pitch
NOBY_GIMBAL_PORT_PITCH_IOPORT=26
# roll
NOBY_GIMBAL_PORT_ROLL_IOPORT=19
# yaw
NOBY_GIMBAL_PORT_YAW_IOPORT=13

# gimbal controlled frequency
# 500Hz



#
class NobyNeckMoverGimbalStorm:
    def __init__(self):
        print("NobyNeckMoverGimbalStorm start")
        self.raspberry = RaspberryIo.RaspberryIo()
        self.raspberry.setPwmFrequency(NOBY_GIMBAL_PORT_PITCH_IOPORT,500)
        self.raspberry.setPwmFrequency(NOBY_GIMBAL_PORT_ROLL_IOPORT,500)
        self.raspberry.setPwmFrequency(NOBY_GIMBAL_PORT_YAW_IOPORT,500)
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


    # 上下向き
    #中心から上下 math.pi/2度までだった気がする
    # 
    def pitch(self,pwmRate):
        print("theta : " + str(pwmRate))
        self.raspberry.setPwmOutput(NOBY_GIMBAL_PORT_PITCH_IOPORT, pwmRate)

    # 顔傾き（はてなのしぐさのやつ）
    # 多くても上下45度
    def roll(self,pwmRate):
        print("theta : " + str(pwmRate))
        self.raspberry.setPwmOutput(NOBY_GIMBAL_PORT_ROLL_IOPORT, pwmRate)


    # 首回転
    # yaw 
    def yaw(self,pwmRate):
        print("theta : " + str(pwmRate))
        self.raspberry.setPwmOutput(NOBY_GIMBAL_PORT_YAW_IOPORT, pwmRate)




