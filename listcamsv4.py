#mporting only those functions 
# which are needed 
from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window 
root = Tk() 
  
# Adding widgets to the root window 
Label(root, text = 'GeeksforGeeks', font =('Verdana', 15)).pack(side = TOP, pady = 10) 
for x in range  (0,2):
    # Creating a photoimage object to use image
    photo = PhotoImage(file = r"blobdance6.gif")
    # here, image option is used to
    # set image on button
    Button(root,  text = str(x), image = photo).pack(side = TOP)
    #Button.config(self.height = 200,self.width = 200)
    print(' Arr ')
'''photo1 = PhotoImage(file = r"blobdance3.gif") 
Button(root, text = 'test !', image = photo1).pack(side = TOP)
photo2=PhotoImage(file = r"blobsanty3.gif") '''
  
mainloop()
