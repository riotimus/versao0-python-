# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:38:09 2020

@author: JOHNJAIRO
"""
import cv2
from tkinter import *
import tkinter.messagebox


'''from Tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()
cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break'''

index = 0
arr = []
while True:
    cap = cv2.VideoCapture(index)
    
    if not cap.read()[0]:
        break
    else:
        
        arr.append(index)
        check, frame = cap.read()
        cv2.imshow("Press enter after the photo to continue", frame)
        #root = Tk() #specify the root window
        #bits=getInfo()
        #label0 = Label( root, text="Press enter")
        #label0.pack()
        #root.mainloop() #Run the "loop" that shows the windows
        #label1 = Label( root, text="Win{0}".format(bits))
        #quit_button = Button(root, text = 'Quit', command=root.destroy())
        cv2.waitKey(0)
    

    cap.release()
    index += 1
#return arr'''
    
    
print(arr)
print(type(arr))
print(len(arr))

'''check, frame = cap.read()
        cv2.imshow("Capturing", frame)'''
