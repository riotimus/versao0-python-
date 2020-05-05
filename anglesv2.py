# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:08:48 2020

@author: JOHNJAIRO
"""

import cv2
import numpy as np

img = cv2.imread('karateCopia.jpg',0)
cv2.imshow("skeleton",img)
cv2.waitKey(0)
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.imshow("skeleton",img)
cv2.waitKey(0)
size = np.size(img)
print('foto abierta  ')
skeleton = np.zeros(img.shape,np.uint8)

ret,img = cv2.threshold(img,127,255,0)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
finished = False

while(not finished):
    eroded = cv2.erode(img,kernel)
    temp = cv2.dilate(eroded,kernel)
    temp = cv2.subtract(img,temp)
    skeleton = cv2.bitwise_or(skeleton,temp)
    img = eroded.copy()
    print('foto em processo  ')

    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        finished = True

cv2.imshow("skeleton",skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()