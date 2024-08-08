import cv2
import numpy as np
import serial
from time import sleep

# 色相によるマスク処理時範囲
RED1_MIN_HSVCOLOR = np.array([0, 150, 80])
RED1_MAX_HSVCOLOR = np.array([30, 240, 255])
RED2_MIN_HSVCOLOR = np.array([150, 150, 80])
RED2_MAX_HSVCOLOR = np.array([179, 240, 255])
BLU1_MIN_HSVCOLOR = np.array([80, 150, 80])
BLU1_MAX_HSVCOLOR = np.array([160, 255, 255])

# シリアル通信の設定
ser = serial.Serial('/dev/ttyUSB0', 115200)


def main():
    second = 0
    # (1) 指定された番号のカメラに対するキャプチャオブジェクトを作成する
    # capture = cv2.VideoCapture(0)

    # (2) 表示用ウィンドウの初期化
    # cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    while ser.is_open:
        # (3) カメラから画像をキャプチャする
        # ret, frame = capture.read()
        # if not ret:
        #     break

        # # RGB画像をHSV画像に変換し、赤色マスク画像を作成
        # red_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # red_mask1 = cv2.inRange(red_hsv, RED1_MIN_HSVCOLOR, RED1_MAX_HSVCOLOR)
        # red_mask2 = cv2.inRange(red_hsv, RED2_MIN_HSVCOLOR, RED2_MAX_HSVCOLOR)
        # red_mask = red_mask1 + red_mask2

        # # RGB画像をHSV画像に変換し、青色マスク画像を作成
        # blu_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # blu_mask = cv2.inRange(blu_hsv, BLU1_MIN_HSVCOLOR, BLU1_MAX_HSVCOLOR)

        # # (4) カメラ画像の表示
        # cv2.imshow("Capture", frame)
        # cv2.imshow("Masked by Red", red_mask)
        # cv2.imshow("Masked by Blue", blu_mask)

        # # 画像の合計ピクセル数を表示
        # red_pixel = cv2.countNonZero(red_mask) / 255
        # blu_pixel = cv2.countNonZero(blu_mask) / 255
        # print(f"Red pixel: {red_pixel}, Blue pixel: {blu_pixel}")

        # 赤色と青色のピクセル数による条件分岐
        try:
            line = ser.readline().decode()
            print(">> " + line)
        except serial.SerialException as e:
            print(f"Serial read error: {e}")
            continue
        
        if second < 50:
            print("Red Up Blue Up")
            ser.write("RUBU".encode())
        elif 50 <= second and second < 100:
            print("Red Up Blue Down")
            ser.write("RUBD".encode())
        elif 100 <= second and second < 150:
            print("Red Down Blue Up")
            ser.write("RDBU".encode())
        else:
            print("Red Down Blue Down")
            ser.write("RDBD".encode())
        ser.flush()
        second += 1
        if second == 200:
            second =0

        # if red_pixel >= 200 and blu_pixel >= 200:
        #     print("Red Up Blue Up")
        #     ser.write("RUBU".encode())
        # elif red_pixel >= 200 and blu_pixel < 200:
        #     print("Red Up Blue Down")
        #     ser.write("RUBD".encode())
        # elif red_pixel < 200 and blu_pixel >= 200:
        #     print("Red Down Blue Up")
        #     ser.write("RDBU".encode())
        # else:
        #     print("Red Down Blue Down")
        #     ser.write("RDBD".encode())

        # (5) 2msecだけキー入力を待つ
        c = cv2.waitKey(2)
        if c == 27:  # Escキー
            break

        # serial通信のdelay
        sleep(1) # 100ms

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()