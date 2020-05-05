import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow,QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

#import Image



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Teste GUI'
        self.left = 10
        self.top = 100
        self.width = 520
        self.height = 500
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setFixedSize(500,500);
        labelA = QLabel(self)
        labelA.setText('  Exercicio  ')
        labelA.move(400, 140)

        self.lb = QLabel(self)
        pixmap = QPixmap("hdd.jpg")
        height_of_label = 300
        self.lb.resize(300, height_of_label)
        self.lb.setPixmap(pixmap.scaled(self.lb.size(), QtCore.Qt.IgnoreAspectRatio))
       # self.show()    
        '''label = QLabel(self)
        pixmap = QPixmap('hdd.jpeg')
        label.setPixmap(pixmap)
        # Optional, resize window to image size
        self.resize(pixmap.width(),pixmap.height())
        
        image = Image.open('image.jpg')
        image.show()
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap("hdd.jpeg"))
        pic.show() # You were missing this.'''
    
        button = QPushButton('Ok', self)
        button.setToolTip('This is an example button')
        button.move(80,170)
        button.clicked.connect(self.on_click)
        
        
        button = QPushButton('Close', self)
        button.setToolTip('This is an example button')
        button.move(170,170)
        button.clicked.connect(self.on_click)
        self.show()
#https://www.e-consystems.com/blog/camera/how-to-access-cameras-using-opencv-with-python/
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())