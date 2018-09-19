
import sys
import time
import threading


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.channel = 0
        self.FLAG_MOVE = False
        self.DIRECTION = 0
        # PCA9685 チャンネルに合わせる
        self.PWM_NUMS = [375, 375, 150, 375, 275]  # 初期値
        self.MINS = [150, 200, 150, 150, 260]  # 最小値
        self.MAXS = [600, 500, 600, 600, 380]  # 最大値
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)
        self.set2def()

    def set2def(self):
        self.pwm.set_pwm(0, 0, self.PWM_NUMS[0])
        self.pwm.set_pwm(1, 0, self.PWM_NUMS[1])
        self.pwm.set_pwm(2, 0, self.PWM_NUMS[2])
        self.pwm.set_pwm(3, 0, self.PWM_NUMS[3])
        self.pwm.set_pwm(4, 0, self.PWM_NUMS[4])

    def run(self):
        print("  === start sub thread ===")

        while True:
            while self.FLAG_MOVE:
                if self.DIRECTION == 1 and self.PWM_NUMS[self.channel] < self.MAXS[self.channel]:
                    self.PWM_NUMS[self.channel] += 1
                elif self.DIRECTION == -1 and self.PWM_NUMS[self.channel] > self.MINS[self.channel]:
                    self.PWM_NUMS[self.channel] -= 1
                self.pwm.set_pwm(self.channel, 0, self.PWM_NUMS[self.channel])
                print("Thread {}. {} {}".format(self.channel,
                                                self.DIRECTION, self.PWM_NUMS[self.channel]))
                time.sleep(0.01)

        print("  === end sub thread ===")


def main():
    th = MyThread()
    th.setDaemon(True)
    th.start()

    device = evdev.InputDevice('/dev/input/event1')
    print(device)
    for event in device.read_loop():
                # event : code sec timestamp() type usec value
        if event.type == evdev.ecodes.EV_KEY:
            print("{} {} {}".format(event.timestamp(), event.code, event.value))
            if event.code == 290:           # Bボタン
                th.channel = 2                     # MG996R 傾き：上
                if event.value == 0:
                    th.FLAG_MOVE = False
                    th.DIRECTION = 0
                elif event.value == 1:
                    th.FLAG_MOVE = True
                    th.DIRECTION = -1

            elif event.code == 291:         # Aボタン
                th.channel = 2                     # MG996R 傾き：上
                if event.value == 0:
                    th.FLAG_MOVE = False
                    th.DIRECTION = 0
                elif event.value == 1:
                    th.FLAG_MOVE = True
                    th.DIRECTION = 1

            elif event.code == 292:         # Lボタン
                th.channel = 3                     # MG996R 手首旋回
                if event.value == 0:
                    th.FLAG_MOVE = False
                    th.DIRECTION = 0
                elif event.value == 1:
                    th.FLAG_MOVE = True
                    th.DIRECTION = -1

            elif event.code == 293:         # Rボタン
                th.channel = 3                     # MG996R 手首旋回
                if event.value == 0:
                    th.FLAG_MOVE = False
                    th.DIRECTION = 0
                elif event.value == 1:
                    th.FLAG_MOVE = True
                    th.DIRECTION = 1

            elif event.code == 288:         # Xボタン
                th.channel = 4                     # MG996R ハンド
                if event.value == 0:
                    th.FLAG_MOVE = False
                    th.DIRECTION = 0
                elif event.value == 1:
                    th.FLAG_MOVE = True
                    th.DIRECTION = 1

            elif event.code == 289:         # Yボタン
                th.channel = 4                     # MG996R ハンド
                if event.value == 0:
                    th.FLAG_MOVE = False
                    th.DIRECTION = 0
                elif event.value == 1:
                    th.FLAG_MOVE = True
                    th.DIRECTION = -1

        elif event.type == evdev.ecodes.EV_ABS:
            print("{} {} {}".format(event.timestamp(), event.code, event.value))

            if event.code == 0:     # X軸,左右
                th.channel = 0     # 旋回
                if event.value == 0:
                    th.FLAG_MOVE = True
                    th.DIRECTION = 1
                elif event.value == 127:
                    th.FLAG_MOVE = False
                    th.DIRECTION = 0
                elif event.value == 255:
                    th.FLAG_MOVE = True
                    th.DIRECTION = -1

            elif event.code == 1:   # y軸,上下
                th.channel = 1     # 傾き：下
                if event.value == 0:
                    th.FLAG_MOVE = True
                    th.DIRECTION = 1
                elif event.value == 127:
                    th.FLAG_MOVE = False
                    th.DIRECTION = 0
                elif event.value == 255:
                    th.FLAG_MOVE = True
                    th.DIRECTION = -1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

print("\n")
sys.exit()
