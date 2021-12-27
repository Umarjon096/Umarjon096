from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import time
import serial
import subprocess
import autoit
from win32api import GetSystemMetrics

winw, winh = GetSystemMetrics(0), GetSystemMetrics(1)
ser = serial.Serial()
ser.port = 'COM7'
ser.open()

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        try:
            # capture from web cam
            cap = cv2.VideoCapture(0)
            detector = cv2.QRCodeDetector()
            ret, cv_img = cap.read()
            data, bbox, _ = detector.detectAndDecode(cv_img)
            if ret:
                self.change_pixmap_signal.emit(cv_img)
                if data:
                    print(data)
                    data = data.encode('ascii')
                    ser.write(data)
                    time.sleep(2)
            # shut down capture system
        except:
            print("Error 99!")
    def stop(self):
        self._run_flag = False
        self.wait()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.Window
            | Qt.WindowStaysOnTopHint  # <<<=====<
        )
        self.setWindowTitle("Project One")
        self.display_width = 640
        self.display_height = 480
        self.image_label = QLabel(self)
        self.image_label.resize(self.display_width, self.display_height)
        # create a text label
        self.textLabel = QLabel('Kamera ')
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        self.setLayout(vbox)
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    a.move(winw - 660, winh - 500)
    sys.exit(app.exec_())
