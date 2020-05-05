#import the library opencv
import cv2
#globbing utility.
import glob
import os
from tkinter import *
from PIL import ImageTk, Image
#select the path
#I have provided my path from my local computer, please change it accordingly
#path = "A:\MY_company\Sanpreet_Singh\Client Work\OpenCV-Sanjeev\images\*.*"

path = r'D:\freelancer\biomecanica\cap*.jpg'
print(path)
x=0
mylist=[]
root = Tk()
for file in glob.glob(path):
    print(file)
    a= cv2.imread(file)
    mylist=[mylist,file]
    #print(a)
    # %%%%%%%%%%%%%%%%%%%%%
    #conversion numpy array into rgb image to show
    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow('Color image', c)
    #wait for 1 second
    k = cv2.waitKey(1000)
    #destroy the window
    cv2.destroyAllWindows()
    x=x+1

print('total de imagenes ',x)
print('list ',mylist)

def func(name):
    print (name)
#mylist = ['item1', 'item2', 'item3']
x=0
for item in mylist:
    print(item)
    item=str(item)
    item = item.replace("[", "")
    print(item)
    item = item.replace("]", "")
    item = item.replace(",", "")
    item = item.replace("'", "")
    #item = item.replace("\\", "\")
    item=os.path.normpath(item)
    print(item)
    print(item.rfind('\\'))
    print(len(item))
    print(' item cap',item[(item.rfind('\\')+1):len(item)])
    #photo = ImageTk.PhotoImage(Image.open(os.path.normpath(item[(item.rfind('\\')+1):len(item)])))
    #Button(root,  text = str(x), image = photo).pack(side = TOP)
    #button = Button(root, text=item, image = photo, command=lambda x=item: func(x))
    button = Button(root, text=item, command=lambda x=item: func(x))
    button.pack()
    x=x+1
    #input("Press Enter to continue...")

root.mainloop()
