# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 02:34:00 2020

@author: JOHNJAIRO
"""

import pyglet
#from tkinter import * 
from PyQt5.QtWidgets import (QWidget, QLabel, 
    QComboBox, QApplication,QPushButton)

animation = pyglet.image.load_animation('gato.gif')
animSprite = pyglet.sprite.Sprite(animation)
 
 
w = animSprite.width
h = animSprite.height
 
window = pyglet.window.Window(width=w, height=h)
 
r,g,b,alpha = 0.5,0.5,0.8,0.8
 
pyglet.gl.glClearColor(r,g,b,alpha)
#lbl = QLabel()
#lbl.setText('text')
        #self.lbl.adjustSize() 

 
@window.event
def on_draw():
    window.clear()
    animSprite.draw()
    ''' lbl = QLabel()
    lbl.setText("text")'''
        #self.lbl.adjustSize() 
 
 
 
pyglet.app.run()