#mporting only those functions 
# which are needed 
from tkinter import * 
from tkinter.ttk import *
import cv2  
from PIL import ImageTk, Image



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
'''print(arr)
print(type(arr))
print(len(arr))'''


# creating tkinter window 
root = Tk() 
  
# Adding widgets to the root window 
Label(root, text = 'GeeksforGeeks', font =('Verdana', 15)).pack(side = TOP, pady = 10)
print(' teste ',(len(arr)))
x=0
for x in range  (0,(len(arr))):
#if x <= (len(arr)):
    print('  autograf ',x)
    filename='captura'+str(x)+'.jpg'
    print(filename)
    # Creating a photoimage object to use image
    photo = ImageTk.PhotoImage(Image.open(filename))
    # here, image option is used to
    # set image on button
    Button(root,  text = str(x), image = photo).pack(side = TOP)
    #Button.config(self.height = 200,self.width = 200)
   # x=x+1
    print(' Arr ',x)
    input("Press Enter to continue...")
    Button.pack()

    
    
    
'''photo1 = PhotoImage(file = r"blobdance3.gif") 
Button(root, text = 'test !', image = photo1).pack(side = TOP)
photo2=PhotoImage(file = r"blobsanty3.gif") '''
#mainloop()


