import cv2
from pyzbar import pyzbar
import time
import serial
last = ""
ser3 = serial.Serial()
ser3.port = 'COM3'
ser3.open()
ser7 = serial.Serial()
ser7.port = 'COM7'
ser7.open()


def read_barcodes(frame):
    global last
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_text = str(barcode.data.decode('utf-8'))
        if "101" in barcode_text:
            if last != barcode_text:
                data = barcode_text.encode('ascii')
                ser3.write(data)
                time.sleep(0.1)
                last = barcode_text
        else:
            data = barcode_text.encode('ascii')
            ser7.write(data)
            time.sleep(0.1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return frame


def main():
    try:
        camera1 = cv2.VideoCapture(1)
        camera2 = cv2.VideoCapture(2)
        while True:
            ret, frame1 = camera1.read()
            ret1, frame2 = camera2.read()
            frame1 = read_barcodes(frame1)
            frame2 = read_barcodes(frame2)
            frame1 = cv2.resize(frame1, (640, 480))
            frame2 = cv2.resize(frame2, (640, 480))
            cv2.imshow('Barcode reader1', frame1)
            cv2.imshow('Barcode reader2', frame2)
            if cv2.waitKey(1) & 0xFF == 27:
                break
    except:
        print("XXX")
    camera1.release()
    camera2.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

