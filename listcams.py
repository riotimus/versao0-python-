# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:38:09 2020

@author: JOHNJAIRO
"""
import cv2

'''cap = cv2.VideoCapture(1)

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
        check, frame = cap.read()
        cv2.imshow("Capturing", frame)
        arr.append(index)
        cv2.waitKey(0)
    

    cap.release()
    index += 1
#return arr'''
    
    
print(arr)
print(type(arr))
print(len(arr))
