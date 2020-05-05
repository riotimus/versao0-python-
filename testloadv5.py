# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:08:04 2020

@author: JOHNJAIRO
"""

'''ps_AniGifPlay2.py
use PySide (public PyQt) to play an animated gif file
depending on your version of Python
you can use the Windows self-extracting installer
PySide-1.2.1.win32-py2.7.exe
PySide-1.2.1.win32-py3.3.exe
from:
http://www.lfd.uci.edu/~gohlke/pythonlibs/
PySide is the official LGPL-licensed version of PyQT
tested with Python27 and Python33  by  vegaseat  11apr2014
'''
import sys 
from PySide.QtCore import *
from PySide.QtGui import * 
class MoviePlayer(QWidget): 
    def __init__(self, parent=None): 
        QWidget.__init__(self, parent) 
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("QMovie to show animated gif")
        
        # set up the movie screen on a label
        self.movie_screen = QLabel()
        # expand and center the label 
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, 
            QSizePolicy.Expanding)        
        self.movie_screen.setAlignment(Qt.AlignCenter) 
        self.btn_start = QPushButton("Start Animation")
        self.btn_start.clicked.connect(self.start)  
        self.btn_stop = QPushButton("Stop Animation")
        self.btn_stop.clicked.connect(self.stop)        
        # positin the widgets
        main_layout = QVBoxLayout() 
        main_layout.addWidget(self.movie_screen)
        main_layout.addWidget(self.btn_start) 
        main_layout.addWidget(self.btn_stop)
        self.setLayout(main_layout) 
                
        # use an animated gif file you have in the working folder
        # or give the full file path
        ag_file = "gato.gif"
        self.movie = QMovie(ag_file, QByteArray(), self) 
        self.movie.setCacheMode(QMovie.CacheAll) 
        self.movie.setSpeed(100) 
        self.movie_screen.setMovie(self.movie) 
        # optionally display first frame
        self.movie.start()
        self.movie.stop()
        
    def start(self):
        """sart animnation"""
        self.movie.start()
        
    def stop(self):
        """stop the animation"""
        self.movie.stop()
# you can replace [] with sys.argv commandline arg 
app = QApplication([]) 
player = MoviePlayer() 
player.show() 
app.exec_()