from PIL import Image
import os, os.path

imgs = []
path = "E:/freelancer/biomecanica/"
valid_images = [".jpg",".gif",".png",".tga"]
print('patghhh  ',path)
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    print(ext)
    if ext.lower() not in valid_images:
        continue
    imgs.append(Image.open(os.path.join(path,f)))