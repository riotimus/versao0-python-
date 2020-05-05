import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow,QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
import time
import threading
#import Image



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
        labelA = QLabel(self)
        labelA.setText('  Exercicio  ')
        labelA.move(400, 140)
        
        labelAB = QLabel(self)
        labelAB.setText('  Nro')
        labelAB.move(400, 180)
        #labelAB.setStyleSheet("QLabel { background-color : blue; color : red; }");
        
        labelB = QLabel(self)
        labelB.setText(' de 40')
        labelB.move(425, 180)
        #labelB.setStyleSheet("QLabel { background-color : red; color : blue; }");
        
        labelC = QLabel(self)
        labelC.setText('    Tempo    ')
        labelC.move(400, 240)
        #labelC.setStyleSheet("QLabel { background-color : red; color : blue; }");
        start = time.time()
        end = time.time()
        print(end - start)
        
        labelCD = QLabel(self)
        labelCD.setText(str(end - start))
        labelCD.move(400, 280)
        
        labelD = QLabel(self)
        labelD.setText('   segundos  ')
        labelD.move(425, 280)
        #labelD.setStyleSheet("QLabel { background-color : red; color : blue; }");
        #printit(self)
        #printit2(self)
        #threading.Timer(15.0, printit).start()
        #time.sleep(15)
        self.lb = QLabel(self)
        pixmap = QPixmap("hdd.jpg")
        self.lb.move(80,90)
        height_of_label = 250
        self.lb.resize(250, height_of_label)
        self.lb.setPixmap(pixmap.scaled(self.lb.size(), QtCore.Qt.IgnoreAspectRatio))
        labelAB = QLabel(self)
        labelAB.setText('  1')
        labelAB.move(400, 180)
        time.sleep(15)
        #self.show()
        print('foto 1')
        #threading.Timer(15.0, printit).start()
        self.lb = QLabel(self)
        pixmap = QPixmap("gato.gif")
        self.lb.move(80,90)
        height_of_label = 250
        self.lb.resize(250, height_of_label)
        self.lb.setPixmap(pixmap.scaled(self.lb.size(), QtCore.Qt.IgnoreAspectRatio))
        labelAB = QLabel(self)
        labelAB.setText('  2')
        labelAB.move(400, 180)
        time.sleep(15)
        #self.show()
        print('foto 2')
        self.lb = QLabel(self)
        pixmap = QPixmap("gatomusical.gif")
        self.lb.move(80,90)
        height_of_label = 250
        self.lb.resize(250, height_of_label)
        self.lb.setPixmap(pixmap.scaled(self.lb.size(), QtCore.Qt.IgnoreAspectRatio))
        labelAB = QLabel(self)
        labelAB.setText('  3')
        labelAB.move(400, 180)
        print('foto 3')

        
       # self.show()    
        
        button = QPushButton('Ok', self)
        button.setToolTip('This is an example button')
        button.move(120,350)
        button.clicked.connect(self.on_click)
        
        
        button = QPushButton('Close', self)
        button.setToolTip('This is an example button')
        button.move(250,350)
        button.clicked.connect(self.on_click)
        self.show()
#https://www.e-consystems.com/blog/camera/how-to-access-cameras-using-opencv-with-python/
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        
    
   # def printit():
        
        
    #def printit():
        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())