# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:19:55 2020

@author: JOHNJAIRO
"""

import cv2
import time
import numpy as np
import filebrowser 

try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
    
    

def listcam():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        
        cap.release()
        index += 1
        #print(arr)
        #print(type(arr))
        #print(len(arr))
    return arr

'''def filebrow(self):
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use("clam")

def c_open_file_old():
    rep = filedialog.askopenfilenames(
    	parent=root,
    	initialdir='/',
    	initialfile='tmp',
    	filetypes=[
    		("mpg", "*.mpg"),
            ("mp4", "*.mp4"),
    		("avi", "*.avi"),
            ("mpeg", "*.mpeg"),
    		("All files", "*")])
    print(rep)
    try:
	    os.startfile(rep[0])
    except IndexError:
        print("No file selected")
   
    return path'''
        
lista=listcam()
print(lista)
path=filebrowser
'''execfile("filebrowser.py 1")
#filebrow(self)

#ttk.Button(self, text="Open files", command=c_open_file_old).grid(row=1, column=0, padx=4, pady=4, sticky='ew')
 
root.mainloop()´'''