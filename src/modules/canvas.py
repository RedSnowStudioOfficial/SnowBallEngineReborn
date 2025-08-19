import tkinter as tk
from tkinter import ttk

class SBTK_Canvas(tk.Canvas):
    
    def __init__(self, parent, **kwargs):
        self.parent = parent
    
        tk.Canvas.__init__(self, parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.canv_wh = [self.winfo_reqwidth(), self.winfo_reqheight()]

        self.coef_wh = [1, 1]
        
        self.config(highlightthickness=0)

        print("Canvas инициализирована", "\n")
        
    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wh_scale = [float(event.width)/self.canv_wh[0], float(event.height)/self.canv_wh[1]]
        
        print(wh_scale)
        
        prev_wh = self.canv_wh
        
        self.canv_wh = [event.width, event.height]
        
        if self.parent.fullScreenState == True: # or self.parent.scale_x > 0 or self.parent.scale_y > 0:
            
            self.coef_wh = [(self.canv_wh[0] / prev_wh[0]), (self.canv_wh[1] / prev_wh[1])]
            
        else:
        
            self.coef_wh = [1, 1]

        # resize the canvas 
        self.config(width=self.canv_wh[0], height=self.canv_wh[1])
        # rescale all the objects tagged with the "all" tag

        self.scale("all", 0, 0, wh_scale[0], wh_scale[1])


    def move_obj(self, ID, x, y):
        self.move(ID, x * self.coef_wh[0], y * self.coef_wh[1])
    
    def move_obj_to(self, ID, x, y):
        self.moveto(ID, x * self.coef_wh[0], y * self.coef_wh[1])

    def update_func_misec(self, func, misec):
        self.update()
        self.after(int(misec), func)