# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:41:08 2020

@author: JOHNJAIRO
"""
import cv2
from tkinter import * 
from PIL import Image, ImageTk
Width=1000
Height=1000

canvas = Image.new("RGB",(Width,Height),"white")
gif = Image.open('gato.gif', 'r')
frames = []
try:
    while 1:
        frames.append(gif.copy())
        gif.seek(len(frames))
except EOFError:
    pass

for frame in frames:
     canvas.paste(frame)
     canvas.show()