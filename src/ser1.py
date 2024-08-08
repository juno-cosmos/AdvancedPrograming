import cv2
import numpy as np
import serial
from time import sleep


# シリアル通信の設定
ser = serial.Serial('/dev/ttyUSB0', 115200)

def main():
    count = 0
    while ser.is_open:
        if count % 100 < 25 and count % 100 >= 0:
            ser.write("RUBU".encode())
        elif count % 100 < 50 and count % 100 >= 25:
            ser.write("RUBD".encode())
        elif count % 100 < 75 and count % 100 >= 50:
            ser.write("RDBU".encode())
        elif count % 100 < 100 and count % 100 >= 75:
            ser.write("RDBD".encode())
        sleep(1)

if __name__ == "__main__":
    main()
