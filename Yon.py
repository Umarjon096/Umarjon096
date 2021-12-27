import cv2
from pyzbar import pyzbar
import time
import serial
#from vaqt import yil, oy, kun, soat, minut, sekund, xafta
#f = open("log.txt", "a")
#f.write("\nProgram started at "+str(yil," ")+str(oy," ")+str(kun,", ")+str(soat,":")+str(minut,":")+str(sekund,", ")+xafta)
last = ""
i = 1
ser3 = serial.Serial()
ser3.port = 'COM3'
ser3.open()


def read_barcodes(frame):
    global last, i
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
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                time.sleep(1)
                #f.write("\n"+barcode_text+"    --    "+str(soat,":")+str(minut,":")+str(sekund))
                cv2.imwrite(filename='saved_img_'+str(i)+'.jpg', img=frame)
        i += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return frame


def main():
    try:
        camera2 = cv2.VideoCapture('rtsp://admin:Admin123@192.168.1.64')
        while True:
            ret1, frame2 = camera2.read()
            frame2 = read_barcodes(frame2)
            frame2 = cv2.resize(frame2, (640, 480))
            cv2.imshow('Barcode reader2', frame2)
            if cv2.waitKey(1) & 0xFF == 27:
                break
    except:
        print("XXX")
        #f.close()
    #f.close()
    camera2.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

