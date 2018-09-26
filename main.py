import cv2


def main():
    print(cv2.__version__)
    # start
    print("start noby eye")

    # 係り受け解析をする
    sendText4Noby("リモコンをとって")
    # リモコンを探す
    #
    # end
    searchObjectAndOrder("リモコン", "とって")
    print("finish noby eye")
    print(" start arm")
    # Arm.move()
    # arm.grusp()
    moveArm(1, 2, 3, 4, 5, 6)
    # finish arm
    print("finish arm")
    cameraOpen()

#
#


def sendText4Noby(sentence):
    print("ノビィに文字を送って形態素解析をしてもらう")
# ものを探す


def searchObjectAndOrder(objectName, orderName):
    print("カメラを動かして画像認識をする")
    moveCamera(2, 3, 4)
    # cv
    objectFromCameraName = searchObjectFromCamera()
    # 目標物が見つかったか
    if objectFromCameraName == objectName:
        print("対象が見つかった")
        moveArm(1, 2, 3, 4, 5, 6)
        doOrder(orderName)
        moveArm(1, 2, 3, 4, 5, 6)
    else:
        print("もう一度探す。ぐるぐるしてもなかったら、見つからない旨の返事をする")

#
# リモコン


def searchObjectFromCamera():
    print("カメラに映った内容を記載する")
    return "リモコン"

# 実行する


def doOrder(orderName):
    print("オーダーの内容:"+orderName)
    # orderの内容をどうにかして分類する
    print("カメラを止めてつかむ")
    # Arm.tukamu();
    # Arm.move();
    print("つかんだら、オーナーのもとにもっていく")
    # カメラをオーナーのほうに向きなおして
    # 手を放す
    # arm.hanasu();
    return True

#
#
#


def moveCamera(x, y, z):
    # camera move camera what something to detect
    print("camera start")
    print("camera end")
# 腕動かすの開始


def moveArm(x, y, z, k, l, m):
    # Armを動かす。
    print(k)
    print(l)
    print(m)
# カメラを開く


def cameraOpen():
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0)  # 0はカメラのデバイス番号
    cap.set(cv2.CAP_PROP_FPS,10)
    #frame = cv2.resize(frame, (int(frame.shape[1]/4), int(frame.shape[0]/4)))
    cap2 = cv2.VideoCapture(1)
    cap2.set(cv2.CAP_PROP_FPS,10);
    while True:
        ret, frame = cap.read()
        ret2,frame2 = cap2.read()
        if(not ret and not ret2):
            print("えらー")

        #frame = cv2.resize(frame, (int(frame.shape[1]/4), int(frame.shape[0]/4)))
        # フレームをリサイズ
        # 色を白黒にする
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #
        retval, bw = cv2.threshold(
            gray, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        #contours, hierarchy= cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        image, contours, hierarchy = cv2.findContours(
            bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        drawContours(frame, contours)
        cv2.imshow('camera capture', frame)
        cv2.imshow('camera2 ',frame2)
        k = cv2.waitKey()
        if k == 27:  # ESCキーで終了
            break
    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()


def drawContours(frame, contours):
    detect_count = 0
    # 各輪郭に対する処理
    for i in range(0, len(contours)):
        area = cv2.contourArea(contours[i])
    # ノイズ（小さすぎる領域）と全体の輪郭（大きすぎる領域）を除外
        if area < 1e2 or 1e5 < area:
            continue
    # 外接矩形
        if len(contours[i]) > 0:
            rect = contours[i]
            x, y, w, h = cv2.boundingRect(rect)
            cv2.imwrite("D:\\project\\noby\\nobyeye\\" + str(detect_count) + ".jpg", frame[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # 外接矩形毎に画像を保存
        # 画像切り出して、もの判別する。
        detect_count = detect_count + 1
    print("detect count");
    print(detect_count);

main()
