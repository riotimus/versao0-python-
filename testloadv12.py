# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 01:13:35 2020

@author: JOHNJAIRO
"""

import pyglet

animation =pyglet.image.load('gato.gif')
animSprite=pyglet.sprite.Sprite(animation) 

w=animSprite.width
h=animSprite.height

windows=pyglet.window.Window(width=w,height=h)

r,g,b,alpha=0.5,0.5,0.8,0.5
pyglet.gl.glClearColor(r,g,b,alpha)

#pyglet.gl.glClearColor(r,g,b,alpha)

def on_draw():
    windows.clear()
    animSprite.draw()
    
    
pyglet.app.run()