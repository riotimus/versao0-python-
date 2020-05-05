#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows how to use 
a QComboBox widget.
 
Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QLabel, 
    QComboBox, QApplication)
import sys
#import filebrowserv1
import cambrowserv1

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.lbl = QLabel("Arquivo", self)
        opc=cambrowserv1.listcam()
        #print('   gghgh  ',opc)
        #print('long  ',len(opc))
        #print(type(opc))

        combo = QComboBox(self)
        combo.addItem("_______")
        combo.addItem("Arquivo")
        for tr in range (len(opc)):
            print('   index  ',opc[tr])
            combo.addItem("Webcam "+str(opc[tr]))
        
        #combo.addItem("Webcam")
        '''combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")'''

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)        
        Button(root, text = 'Cam', image = img).pack(side = TOP)  
        #self.setGeometry(300, 300, 300, 200)
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('Fonte video')
        self.show()
        
        
    def onActivated(self, text):
      
        self.lbl.setText(text)
        self.lbl.adjustSize()  
        print(' fuente video  ',text,'   ',type(text),'   ',len(text))
        #print()
        '''if (text=="Webcam"):
            print('llamado cambrowser')
            cambrowser.listcam()
        elif (text=='Arquivo'):
            print('llamadao filebreo')
            filebrowserv1
        else:
            print('no opcion')'''
                
                
        
        #return text
                
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())