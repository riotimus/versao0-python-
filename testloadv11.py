# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:55:32 2020

@author: JOHNJAIRO
"""

from tkinter import *
     
canvas = Canvas(width=300, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)                
     
photo=PhotoImage(file='gato.gif')
canvas.create_image(250, 0, image=photo, anchor=NW)
     
     
widget = Label(canvas, text='AAA', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)      
mainloop()