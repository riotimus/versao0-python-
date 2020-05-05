# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:58:41 2020

@author: JOHNJAIRO
"""

try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
 
 
root = tk.Tk()
 
style = ttk.Style(root)
style.theme_use("clam")
 
 
def c_open_file_old():
    rep = filedialog.askopenfilenames(
    	parent=root,
    	initialdir='/',
    	initialfile='tmp',
    	filetypes=[
    		("mpg", "*.mpg"),
            ("mp4", "*.mp4"),
    		("avi", "*.avi"),
            ("mpeg", "*.mpeg"),
    		("All files", "*")])
    #print(rep)
    return rep
    try:
	    os.startfile(rep[0])
    except IndexError:
        print("No file selected")
 
ttk.Button(root, text="Open files", command=c_open_file_old).grid(row=1, column=0, padx=4, pady=4, sticky='ew')
 
root.mainloop()