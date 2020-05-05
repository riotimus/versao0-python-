# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:47:28 2020

@author: JOHNJAIRO
"""

import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import cv2

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

root = tk.Tk()
lbl = ImageLabel(root)
lbl.place(anchor = 'nw')
lbl.pack()
lbl.load('gato.gif')
cv2.waitKey(100)
#lbl = ImageLabel(root)
lbl.place(anchor = 'nw')
lbl.pack()
lbl.load('gatomusical.gif')
'''https://stackoverflow.com/questions/38660528/putting-gif-image-in-tkinter-window'''
root.mainloop()


