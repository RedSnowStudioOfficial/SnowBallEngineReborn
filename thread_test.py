from src.SBTK_CORE import *

root = sbtkgamewindow(width=320, height=180)

inputs = sbtkinput(root.window, "Left", "Right", "Up", "Down", "w", "s")

images = tk.PhotoImage(file="resources\\images\\Player_Sprites.png")
palletes =tk.PhotoImage(file="resources\\images\\palletes.png")

background_color = (64, 192, 64)
furr_color = (252, 144, 0)

#Загрузка спрайтов по комплектам анимаций
#RUN

rota_test = sbtkanimation()
rota_test.add_frame_end_crop("run1", images, 2, 74, 56, 32)
#rota_test._Start.image = rota_test._Start.get_rotated_90deg_to_right_image()
#rota_test._Start.image = rota_test._Start.get_rotated_90deg_to_right_image()
#rota_test._Start.image = rota_test._Start.get_rotated_90deg_to_right_image()

#rota_test._Start.image = rota_test._Start.get_mirrored_horizontal_image()

#rota_test._Start.image = rota_test._Start.get_mirrored_vertical_image()

rota_test._Start.image = rota_test._Start.get_rotated_image_PIL2TK(45)
rota_test._Start.image = rota_test._Start.get_rotated_image_PIL2TK(45)

#rota_test.scale_all_frames_PILL2TK(2.4)

run = sbtkanimation()
run.add_frame_end_crop("run1", images, 2, 74, 56, 32)
run.add_frame_end_crop("run2", images, 60, 74, 56, 32)
run.add_frame_end_crop("run3", images, 118, 74, 56, 32)
run.add_frame_end_crop("run4", images, 176, 74, 56, 32)

#Удаление заднего фона
run.set_all_frames_transperent_color(background_color)

run_water = sbtkanimation()
run_water.copy_animation("_water", run)

run_water.set_all_frames_pallete(palletes, 0, 2)

run.scale_all_frames_PILL2TK(4.8, 2)
run.rotate_all_frames_PILL2TK(22)
run_water.scale_all_frames_PILL2TK(4.8, 2)
run_water.rotate_all_frames_PILL2TK(22)

root.canvas.create_rectangle(0, 0, 200, 100, fill="white")
unders = root.canvas.create_image(0, 0, image=run_water._Start.image)

root.canvas.create_rectangle(0, 100, 800, 100+600, fill="blue")
ups = root.canvas.create_image(0, 0, image=run._Start.image)

test1 = root.canvas.create_image(50, 50, image=rota_test._Start.image)
test2 = root.canvas.create_image(0, 0, image=run_water._Start.image)
test3 = root.canvas.create_image(0, 0, image=run._Start.image)
test4 = root.canvas.create_image(0, 0, image=run_water._Start.image)
test5 = root.canvas.create_image(0, 0, image=run._Start.image)
test6 = root.canvas.create_image(0, 0, image=run_water._Start.image)
test7 = root.canvas.create_image(0, 0, image=run._Start.image)
test8 = root.canvas.create_image(0, 0, image=run_water._Start.image)
test9 = root.canvas.create_image(0, 0, image=run._Start.image)
test10 = root.canvas.create_image(0, 0, image=run_water._Start.image)

transition_hit_box = root.canvas.create_rectangle(-1, -1, 1, 1, fill="black")

delay : float = 10

x_move = 0.2

timer = 400

def update_loop():
    global delay, x_move, timer

    if inputs.is_pressed["Right"]: 
        root.move_object(ups, 0.2, 0)
        root.move_object(unders, 0.2, 0)
        root.move_object(transition_hit_box, 0.2, 0)     
    if inputs.is_pressed["Left"]: 
        root.move_object(ups, -0.2, 0)
        root.move_object(unders, -0.2, 0)
        root.move_object(transition_hit_box, -0.2, 0)
    if inputs.is_pressed["Up"]: 
        root.move_object(ups, 0, -0.2)
        root.move_object(unders, 0, -0.2)
        root.move_object(transition_hit_box, 0, -0.2)
    if inputs.is_pressed["Down"]: 
        root.move_object(ups, 0, 0.2)
        root.move_object(unders, 0, 0.2)
        root.move_object(transition_hit_box, 0, 0.2)

    if inputs.is_pressed["w"]: 
        root.canvas.tag_raise(unders, ups)
    if inputs.is_pressed["s"]: 
        root.canvas.tag_raise(ups, unders)



    timer -= 0.1

    

    if timer <= 0.0:
        root.canvas.moveto(test1, -100.0, random.randint(0, 180))
        root.canvas.moveto(test2, -100.0, random.randint(0, 180))
        root.canvas.moveto(test3, -100.0, random.randint(0, 180))
        root.canvas.moveto(test4, -100.0, random.randint(0, 180))
        root.canvas.moveto(test5, -100.0, random.randint(0, 180))
        root.canvas.moveto(test6, -100.0, random.randint(0, 180))
        root.canvas.moveto(test7, -100.0, random.randint(0, 180))
        root.canvas.moveto(test8, -100.0, random.randint(0, 180))
        root.canvas.moveto(test9, -100.0, random.randint(0, 180))
        root.canvas.moveto(test10, -100.0, random.randint(0, 180))
        timer = 400



   # print(timer)



    root.move_object(test1, x_move, 0)
    root.move_object(test2, x_move, 0)
    root.move_object(test3, x_move, 0)
    root.move_object(test4, x_move, 0)
    root.move_object(test5, x_move, 0)
    root.move_object(test6, x_move, 0)
    root.move_object(test7, x_move, 0)
    root.move_object(test8, x_move, 0)
    root.move_object(test9, x_move, 0)
    root.move_object(test10, x_move, 0)



        #root.canvas.itemconfig(swap_img, image=swap_test.image)
    #if inputs.is_pressed["s"]:
    #if get_overlap(transition_hit_box) and 
        #root.canvas.tag_raise(ups, unders)
        #root.canvas.itemconfig(swap_img, image=swap_test2.image)

    root.update_func_misec(update_loop, 1)

def animation_update():

    if root.window.fullScreenState == True:
        
        run_water.play_animation()
        run.play_animation()
        root.canvas.itemconfig(ups, image=run.get_current_image())
        root.canvas.itemconfig(unders, image=run_water.get_current_image())
        
        root.canvas.itemconfig(test1, image=run_water.get_current_image())
        root.canvas.itemconfig(test2, image=run_water.get_current_image())
        root.canvas.itemconfig(test3, image=run_water.get_current_image())
        root.canvas.itemconfig(test4, image=run_water.get_current_image())
        root.canvas.itemconfig(test5, image=run_water.get_current_image())
        root.canvas.itemconfig(test6, image=run_water.get_current_image())
        root.canvas.itemconfig(test7, image=run_water.get_current_image())
        root.canvas.itemconfig(test8, image=run_water.get_current_image())
        root.canvas.itemconfig(test9, image=run_water.get_current_image())
        root.canvas.itemconfig(test10, image=run_water.get_current_image())
    else:

        #root.canvas.itemconfig(img, image=swap_anim.get_current_image())
        pass
    root.update_func_misec(animation_update, 1)

# Create threads for function1 and function2
thread1 = thread.Thread(target=update_loop)
thread2 = thread.Thread(target=animation_update)

# Start the threads
thread1.start()
thread2.start()

root.start_gameloop()