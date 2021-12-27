import cv2
import serial
import time

f = open("errorlog.txt", 'w')

start_time = int(time.time())
last_time = 0
ser4 = serial.Serial()
ser4.port = 'COM3'
ser4.open()
ser7 = serial.Serial()
ser7.port = 'COM7'
ser7.open()

try:
    cap = cv2.VideoCapture(2)
except:
    cap = cv2.VideoCapture(0)
try:
    cap2 = cv2.VideoCapture(1)
except:
    cap2 = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()
i = 0
last = ""

while True:
    try:
        ret, img = cap.read()
        ret2, img2 = cap2.read()
        gray = cv2.resize(img, (640, 480))
        data, bbox, _ = detector.detectAndDecode(gray)
        gray2 = cv2.resize(img2, (320, 240))
        data2, bbox2, _2 = detector.detectAndDecode(gray2)

        if data:
            if "101" in str(data) and str(data) != last:
                data = data.encode('ascii')
                ser4.write(data)
                last = str(data)
            elif "101" not in str(data):
                data = data.encode('ascii')
                ser7.write(data)
            data = ""
        if data2:
            if "101" in str(data2) and str(data2) != last:
                data2 = data2.encode('ascii')
                ser4.write(data2)
                last = str(data2)
            elif "101" not in str(data2):
                data2 = data2.encode('ascii')
                ser7.write(data2)
            data2 = ""
        cv2.imshow("QR Code1", gray)
        cv2.imshow("QR Code2", gray2)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    except:
        err_time = int(time.time()) - start_time
        i += 1
        f.write(str("Davomiylik vaqti: " + str(err_time) + " sekund\n"))
        f.write(str("Oxirgi bexato ishlashi: " + str(err_time - last_time) + " sekund\n"))
        f.write(str("O'rtacha xatolik: " + str(int(err_time / i)) + " sekund\n"))
        last_time = err_time


cap.release()
cv2.destroyAllWindows()
