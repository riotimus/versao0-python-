# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 12:43:43 2020

@author: JOHNJAIRO
"""
import os.path
from skimage.io import imread_collection
import skimage
import cv2
from tkinter import * 
from PIL import Image, ImageTk

try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog


#your path 
col_dir = 'E:/freelancer/biomecanica/*.gif'
root = Tk()

#creating a collection with the available images
col = imread_collection(col_dir)
for i in range(len(col)):
    #print(i)
    picture = col[i]
    #print('  fgg ',type(picture))
        #print('   fff  ',picture)
    picture = skimage.color.rgb2gray(picture)
    cv2.imshow('test',picture)
    
    #anim = tk.Label(root, picture)
    #anim.pack()
    cv2.waitKey(50)
        
print('path   ',col, 'type  ',type(col))
col = os.path.normpath(str(col))
'''print()
print()'''
print('path norm  ',col,'  type ',type(col),'   ',len(col))