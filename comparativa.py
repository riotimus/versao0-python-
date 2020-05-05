from PIL import ImageChops, Image , ImageDraw
import math, operator
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.clf()
plt.cla()
plt.close()


def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox()
#is None



im1=Image.open('estiramento.jpg')
im2=Image.open('estiramentov1.jpg')
#im2=Image.open('blobsanty2.gif')



im3=ImageChops.difference(im1, im2)
plt.imshow(im3)
#im3.show() 
im4=equal(im1,im2)
draw = ImageDraw.Draw(im1)
draw.rectangle(im4)
print(' teste ')
print(' tipo ',type(im4))
print('var  ',im4)
#im3.rectangle(im4, fill ="# ffff33", outline ="red") 
#plt.gca().add_patch(Rectangle((50,100),40,30,linewidth=1,edgecolor='r',facecolor='none'))
plt.ion()
plt.show()
