# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:32:02 2020

@author: JOHNJAIRO
"""

from tkinter import * 
from PIL import Image, ImageTk
import cv2


class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)        


root = Tk()

#col_dir = 'E:/freelancer/biomecanica/*.gif'
#root = Tk()

#creating a collection with the available images
#col = imread_collection(col_dir)


anim = MyLabel(root, 'gato.gif')
anim.pack()
cv2.waitKey(50)
anim = MyLabel(root, 'gatomusical.gif')
anim.pack()

def stop_it():
    anim.after_cancel(anim.cancel)

Button(root, text='stop', command=stop_it).pack()

root.mainloop()