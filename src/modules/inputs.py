import tkinter as tk
from tkinter import ttk

class SBTK_Inputs:
    
    def __init__(self, parent, *args) -> None:
        self.parent = parent
        
        self.bindings = list(args)
        
        self.is_pressed = {}
        
        self.set_bindings()
        
        print("Inputs активированна", "\n")

    def key_pressed(self, event):
        self.is_pressed[event.keysym] = True

    def key_released(self, event):
        self.is_pressed[event.keysym] = False

    # def is_pressing(self):
        # for keys in self.bindings:
            # if self.is_pressed[keys] == True:
                # return True
            # else:
                # return False

    def set_bindings(self):
        for keys in self.bindings:
            self.parent.bind("<KeyPress-%s>" % keys, self.key_pressed)
            self.parent.bind("<KeyRelease-%s>" % keys, self.key_released)
            self.is_pressed[keys] = False
