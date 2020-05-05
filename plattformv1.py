from tkinter import *
import tkinter.messagebox

def getInfo():
    try:
        os.environ["(x86)"]
        bits = 64
    except:
        bits = 32
        print ("Win{0}".format(bits))
    return bits

def quit():
    #This function closes the root window
    root.destroy()


root = Tk() #specify the root window
bits=getInfo()
label0 = Label( root, text="Plataforma actual")

label1 = Label( root, text="Win{0}".format(bits))

quit_button = Button(root, text = 'Quit', command=quit) #specify the quit button that quits the main window when clicked

#Add the items we specified to the window
label0.pack()
label1.pack()
#E1.pack()
#submit.pack(side =BOTTOM)
quit_button.pack(side =BOTTOM) 

root.mainloop() #Run the "loop" that shows the windows
