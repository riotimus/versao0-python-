from PIL import Image
from pylab import *
import cv2

# read image to array
image = array(Image.open('OpenPose_sample_image.png').convert('L'))

ret,thresh = cv2.threshold(image,245,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

tam = 0

for contorno in contours:
    if len(contorno) > tam:
        contornoGrande = contorno
        tam = len(contorno)

cv2.drawContours(image,contornoGrande.astype('int'),-1,(0,255,0),2)

cv2.imshow('My image',image)

cv2.waitKey()
cv2.destroyAllWindows()
