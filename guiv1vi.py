# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:01:04 2020

@author: JOHNJAIRO
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label

class Test(App):
    def build(self):
        #return Button(text='load webcam  ', pos=(300,350), size_hint = (.25, .18))
        return Button(text='ok', pos=(100,350), size_hint = (.25, .18))
        #return Label(text="Hello Label", font_size='30')
        #return Label(text='Fonte video', pos=(100,350),font_size='30')
    
    
Test().run()
    