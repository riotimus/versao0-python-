# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:45:08 2020

@author: JOHNJAIRO
"""

from tkinter import *
import time
import os
root = Tk()

frames = [PhotoImage(file='gato.gif',format = 'gif -index %i' %(i)) for i in range(100)]

def update(ind):

    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()