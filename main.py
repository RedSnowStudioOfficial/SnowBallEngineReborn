from src.SBTK_CORE import *
from FPS_Test import FPSMonitor

root = sbtkgamewindow("SnowBallEngineTK")

inputs = sbtkinput(root.window, "Left", "Right", "Up", "Down")
inputs2 = sbtkinput(root.window, "a", "d", "w", "s")

p1 = root.canvas.create_rectangle(10, 10, 30, 50, fill="red")
p2 = root.canvas.create_rectangle(100, 10, 100+20, 50, fill="blue")

#img1 = root.canvas.create_image(200, 50, image=spr1.Get_ImageTk())
#img2 = root.canvas.create_image(50, 50, image=spr2.Get_ImageTk())

def game_loop():
    #Обновляемый код игры

    if inputs.is_pressed["Up"]: 
        root.move_object(p1, 0, -0.2)
    if inputs.is_pressed["Down"]: 
        root.move_object(p1, 0, 0.2)
    if inputs.is_pressed["Left"]: 
        root.move_object(p1, -0.2, 0)
    if inputs.is_pressed["Right"]: 
        root.move_object(p1, 0.2, 0)

    if inputs2.is_pressed["w"]: 
        root.move_object(p2, 0, -0.2)
    if inputs2.is_pressed["s"]: 
        root.move_object(p2, 0, 0.2)
    if inputs2.is_pressed["a"]: 
        root.move_object(p2, -0.2, 0)
    if inputs2.is_pressed["d"]: 
        root.move_object(p2, 0.2, 0)
    
    #root.canvas.itemconfig(img1, image=spr1.Get_ImageTk())



    root.update_func_misec(game_loop, 1)

def animation_update():
    pass
    

game_loop()
animation_update()

root.start_gameloop()