#!/usr/bin/python
from os import listdir
from PIL import Image as PImage
import os
#import Image

def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    #print(' paths',os.getcwd(imagesList[0]))
    print(' path1 ',imagesList[0])
    print(path+'\\'+imagesList[0])
    print('path loadimages  ',path)
    #print('imagelist  ',imagesList)
    loadedImages = []
    for image in imagesList:
        print('   ',path,'  ',image)
        print('  concatenado ',path+image)
        pathnovo=path + image
        print(os.path.normpath(pathnovo))
        #img = Image.open(pathnovo)
        img = PImage.open(path + image)
        loadedImages.append(img)

    return loadedImages

path = os.getcwd()
print(' path   ',path)
# your images in an array
path=path+'\\'
#
print(' path   ',path)
#path=os.path.normpath(path)
imgs = loadImages(path)
print('saida algor  ',imgs,'  ',type(imgs))
for img in imgs:
    # you can show every image
    img.show()
