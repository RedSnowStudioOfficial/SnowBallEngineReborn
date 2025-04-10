from .window import SBTK_Window as sbtkwin
from .canvas import SBTK_Canvas as sbtkcanva

class SBTK_GameWindow:
    def __init__(self, win_name : str = "SBTK_GAME_WIN",
                width : int = 320, height : int = 240,
                rszable : bool = False,
                win_bg : str = "black",
                canva_bg : str = "black"):
        
        self.window = sbtkwin(win_name, width, height, rszable, win_bg)
        self.canvas = sbtkcanva(self.window, width=width, height=height, bg=canva_bg)
    
    def move_object(self, ID, x, y):
        self.canvas.move_obj(ID, x, y)
    
    def update_func_misec(self, func, misec):
        self.canvas.update_func_misec(func, misec)
    
    def start_gameloop(self):
        self.window.start_sbtkloop(self.canvas)