# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

from timeit import default_timer as timer
import numpy as np
import cv2



def time_fn(fn, img, iters=1):
    start = timer()
    result = None
    for i in range(iters):
        result = fn(img)
    end = timer()
    return (result,((end - start) / iters) * 1000)

def run_test(img):
#    res, t = time_fn(fn, img, 4)

    #cv2.imwrite("skeleton_%d.png" % i, res[0])

    #print ("Variant %d" % i)
    print ("Input size = (%d, %d)" % img.shape[:2])
    print ("Ran %d iterations to find skeleton." % res[1])
    print ("Avg. find_skeleton time = %0.4f s." % (t/1000))
    
    

# Create a decent size test image...
img = cv2.imread('karate.jpg',0)
#img = cv2.resize(img, (2048, 2048))
cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
print('fggghh')
run_test(img)