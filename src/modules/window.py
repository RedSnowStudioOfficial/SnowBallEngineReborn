import tkinter as tk
from tkinter import ttk

class SBTK_Window(tk.Tk):
    
    def __init__(self,
                title:str="SBTK_Window",
                width:int=320, height:int=240,
                rszable:bool=True, bg_color:str="black"):

        tk.Tk.__init__(self)
        
        self.title(title)
        
        self.geometry(str(width) + "x" + str(height))
        
        self.resizable(rszable, rszable)
        
        self.canva = None
        
        self.attributes('-fullscreen', False)
        self.fullScreenState = False
        self.bind("<F4>", self.toggle_fullscreen)
        self.bind("<Escape>", self.quit_fullscreen)
        
        self.config(highlightthickness=0)
        self.config(bg=bg_color)
        
        print("Window инициализирована", "\n")
        
    def toggle_fullscreen(self, event):
        
        if self.fullScreenState == False:
            scr_wh = [self.winfo_screenwidth(), self.winfo_screenheight()]
            win_wh = [self.winfo_width(), self.winfo_height()]
            
            #Находим минимальный коэффициент
            min_scale = min(scr_wh[0] / win_wh[0], scr_wh[1] / win_wh[1])
            
            #Умножаем разрешение окна на минимальный коэффициент
            min_wh = [win_wh[0] * min_scale, win_wh[1] * min_scale]
            
            #Записываем разность размеров экрана и максимального разрешения окна отностильно экрана деля её на 2
            curr_wh = [(scr_wh[0] - min_wh[0]) / 2, (scr_wh[1] - min_wh[1]) / 2]
            
            #Обновляем отступы для экрана
            self.canva.pack_configure(padx=curr_wh[0], ipadx=curr_wh[0], pady=curr_wh[1], ipady=curr_wh[1])
            
            self.fullScreenState = True
            self.attributes("-fullscreen", self.fullScreenState)
        
    def quit_fullscreen(self, event):
        self.canva.pack_configure(padx=0, ipadx=0, pady=0, ipady=0)
        self.fullScreenState = False
        self.attributes("-fullscreen", self.fullScreenState)
    
    def start_sbtkloop(self, canva):
        self.canva = canva
        canva.pack(expand=True, fill="both")
        self.mainloop()
    
    def update_func_misec(self, func, misec):
        self.update()
        self.after(int(misec), func)
        
if __name__ == "__main__":
    win = SBTK_Window()
    
    def main_update():
        
        #Основной цикл игры
        print("1")
        
        win.update_func_misec(main_update, 1)

    main_update()
    
    win.mainloop()
    
    
    
