try:
    import Tkinter as Tk
except ImportError:
    import tkinter as Tk

#from PIL import ImageTk
import cv2
#globbing utility.
import glob
import os
from PIL import ImageTk, Image

def clicked(arg):
    print('You clicked {}'.format(arg))




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
       # cv2.waitKey(0)
        filename='captura'+str(index)+'.jpg'
        dim = (80, 80)
        # resize image
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(filename, frame)
    

    cap.release()
    index += 1
    
cv2.destroyAllWindows()   
path = r'D:\freelancer\biomecanica\cap*.jpg'
print(path)
x=0
mylist=[]
root = Tk.Tk()
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
#print('list ',mylist)


btn = Tk.Button(command = lambda: clicked('0'))
btn.img = ImageTk.PhotoImage(file='captura0.jpg')
btn.config(image=btn.img)
btn.pack(side=Tk.LEFT)

btn = Tk.Button(command = lambda: clicked('1'))
btn.img = ImageTk.PhotoImage(file='captura1.jpg')
btn.config(image=btn.img)
btn.pack(side=Tk.LEFT)

Tk.mainloop()
