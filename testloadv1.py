# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 12:40:06 2020

@author: JOHNJAIRO
"""

import glob
import cv2

cv_img = []
for img in glob.glob("E:/freelancer/biomecanica/*.gif"):
    n= cv2.imread(img)
    cv_img.append(n)