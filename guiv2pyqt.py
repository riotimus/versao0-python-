import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Teste GUI'
        self.left = 10
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Ok', self)
        button.setToolTip('This is an example button')
        button.move(80,170)
        button.clicked.connect(self.on_click)
        
        
        button = QPushButton('Close', self)
        button.setToolTip('This is an example button')
        button.move(170,170)
        button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())