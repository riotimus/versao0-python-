import cv2
import os
import glob
from os import listdir

img_dir = "D:\freelancer\biomecanica" # Enter Directory of all images
print(' path img ',img_dir)
data_path = os.path.join(img_dir,'*g')
print(' data path  ',data_path)
files = glob.glob(data_path)
data = []
for f1 in files:
    img = cv2.imread(f1)
    data.append(img)
