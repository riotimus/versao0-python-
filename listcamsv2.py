# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:38:09 2020

@author: JOHNJAIRO
"""
import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow,QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Teste GUI'
        self.left = 10
        self.top = 100
        self.width = 480
        self.height = 450
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(480,450);
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
            cv2.waitKey(0)

    cap.release()
    index += 1
    print(arr)
    print(type(arr))
    print(len(arr))
#return arr

    

'''check, frame = cap.read()
        cv2.imshow("Capturing", frame)'''
