from src.SBTK_CORE import *

root = sbtkgamewindow("SnowBallEngineTK")

spr1 = sbtksprite("test")
spr1.Add_Image_From_Path_Crop("resources/images/Player_Sprites.png", 2, 2, 24, 32)
spr1.Set_Color_To_Color((64, 192, 64, 255), (0, 0, 0, 0))
#spr1.Set_Scale(3.6, 3.6)

#Двойная ротация спрайта с использованием PILL вызывает визуальные артефакты
#spr1.Set_Rotation(45)

spr2 = sbtksprite("getter")
spr2.Add_Image_From_Image(spr1.Get_Scaled_Image(6.3, 6.3))
spr2.Set_Rotation(45)

inputs = sbtkinput(root.window, "Left", "Right", "Up", "Down")
inputs2 = sbtkinput(root.window, "a", "d", "w", "s")

p1 = root.canvas.create_rectangle(10, 10, 30, 50, fill="red")
p2 = root.canvas.create_rectangle(100, 10, 100+20, 50, fill="blue")

img1 = root.canvas.create_image(200, 50, image=spr1.Get_ImageTk())
img2 = root.canvas.create_image(50, 50, image=spr2.Get_ImageTk())

def game_loop():
    #Обновляемый код игры

    if inputs.is_pressed["Up"]: 
        root.move_object(img1, 0, -0.2)
    if inputs.is_pressed["Down"]: 
        root.move_object(img1, 0, 0.2)
    if inputs.is_pressed["Left"]: 
        root.move_object(img1, -0.2, 0)
    if inputs.is_pressed["Right"]: 
        root.move_object(img1, 0.2, 0)

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