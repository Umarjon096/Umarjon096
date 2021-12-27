import cv2
import time
from pyzbar import pyzbar
from datetime import datetime
import serial
cam = open("CamNo.txt", "r")
camN0 = int(cam.read())
cam.close()
now = datetime.now()
d2 = now.strftime("%Y-yil %d-%B, %A, %H:%M:%S")
f = open("log.txt", "a")
f.write("\n Program started at "+str(d2))
last = ""
i = 1
ser7 = serial.Serial()
ser7.port = 'COM7'
ser7.open()


def read_barcodes(frame):
    global last, i, now, d2
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        now = datetime.now()
        d2 = now.strftime("%Y-yil %d-%B, %A, %H:%M:%S")
        x, y, w, h = barcode.rect
        barcode_text = str(barcode.data.decode('utf-8'))
        data = barcode_text.encode('ascii')
        ser7.write(data)
        f.write("\n"+barcode_text + "    --    " + d2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imwrite(filename='saved_img_'+str(i)+'.jpg', img=frame)
        i += 1
        time.sleep(2)
    return frame


def main():
    try:
        camera1 = cv2.VideoCapture(camN0)
        while True:
            ret, frame1 = camera1.read()
            frame1 = read_barcodes(frame1)
            frame1 = cv2.resize(frame1, (640, 480))
            cv2.imshow('Barcode reader1', frame1)
            if cv2.waitKey(1) & 0xFF == 27:
                break
    except:
        print("XXX")
        f.close()
    f.close()
    camera1.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

