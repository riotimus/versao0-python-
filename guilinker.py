# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:31:34 2020

@author: JOHNJAIRO
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic

#class Mypose(QtWidgets.QMainWindow):
class Mypose(QtWidgets.QDialog):
    def __init__(self):
        super(Mypose,self).__init__()
        uic.loadUi('Guiv0.ui',self)
        
        

if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window= Mypose()
    window.show()
    sys.exit(app.exec())

