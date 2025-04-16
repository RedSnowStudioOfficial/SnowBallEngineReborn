from src.SBTK_CORE import *
import threading as th
import subprocess as sp
from PIL import ImageTk, Image

root = sbtkgamewindow()

class Frame:
    def __init__(self, image):
        self.image = image
        self.nextFrame = None
        self.prevFrame = None

class AnimationTK:
    def __init__(self) -> None:
        self._Start = None
        self._End = None

        self.step : float = 0.1 #Шаг анимации
        self.delay : float = 10 #Промежуток между кадрами
        self.timer : float = 0.0 #Осноной таймер

        self.p = self._Start

    def add_frame_end_crop(self, source_image, x, y, width, height):
        
        crop_image = tk.PhotoImage(width=width, height=height)

        for i in range(0, width):
            for j in range(0, height):
                crop_image.put('#%02x%02x%02x' % source_image.get(x+i, y+j), to=(i, j))
        
        new_frame = Frame(crop_image)

        if self._Start == None:
            self._Start = new_frame
            self._End = new_frame
        else:
            self._End.nextFrame = new_frame
            self._End = new_frame

    def add_frames_end_image(self, source_image):
        image = tk.PhotoImage.copy(source_image)
        
        new_frame = Frame(image)
        if self._Start == None:
            self._Start = new_frame
            self._End = new_frame
        else:
            self._End.nextFrame = new_frame
            self._End = new_frame

    def copy_animation_frames(self, animTK):
        j = animTK._Start

        for z in range(animTK.get_count_frames()):
            if j != None:
                new_image = j.image.copy()
                self.add_frames_end_image(new_image)
                j = j.nextFrame
            
    def set_transperent_color_rgb(self, image, color):
        width, height = image.width(), image.height()
    
        #Удаление заднего слоя на прозрачность
        #Пробегаемся по пикселям картинки
        for x in range(width): #Берём параметр ширины и высоты и пробегаемся по всем пиксялям
            for y in range(height):
                if image.get(x, y) == color:
                    image.transparency_set(x, y, 1)

    def scale_frame(self, image, scale):
        
        if scale < 0:
            return image.subscale(abs(scale), abs(scale))
        elif scale > 0:
            return image.zoom(scale, scale)
        elif scale == 0:
            return image

    def get_count_frames(self):
        p = self._Start
        counter = 0

        while p != None:
            counter = counter + 1
            p = p.nextFrame
            
        
        return counter

    def scale_all_frames(self, scale):
        p = self._Start

        for i in range(self.get_count_frames()):
            p.image = self.scale_frame(p.image, scale)
            p = p.nextFrame

        print("DONE")

    def play_anim_once(self):
        if self.p != None:
            self.timer += self.step
            if self.timer >= self.delay:
                self.timer = 0.0
                
                self.p = self.p.nextFrame
                
        else:
            self.p = self._Start
            return

    def play_anim_loop(self):
        if self.p != None:
            self.timer += self.step
            if self.timer >= self.delay:
                self.timer = 0.0
                
                self.p = self.p.nextFrame
                
        else:
            self.p = self._Start

    def get_current_frame(self):
        if self.p != None:
            return self.p
    
    def get_current_image(self):
        if self.p != None:
            return self.p.image

inputs = sbtkinput(root.window, "Left", "Right", "Up", "Down", "w", "s")

images = tk.PhotoImage(file="resources\images\Player_Sprites.png")

background_color = (64, 192, 64)

anim_min_scr = AnimationTK()
anim_min_scr.add_frame_end_crop(images, 2, 74, 56, 32)
anim_min_scr.add_frame_end_crop(images, 60, 74, 56, 32)
anim_min_scr.add_frame_end_crop(images, 118, 74, 56, 32)
anim_min_scr.add_frame_end_crop(images, 176, 74, 56, 32)

print(anim_min_scr.get_count_frames())

anim_max_scr = AnimationTK()
anim_max_scr.copy_animation_frames(anim_min_scr)

anim_max_scr.scale_all_frames(3)

print(anim_max_scr.get_count_frames())

x, y, w, h = 10, 10, 20, 40

img = root.canvas.create_image(x, y, image=anim_min_scr._Start.image)

p1 = root.canvas.create_rectangle(x, y, w, h, fill="red")

def update_loop():
    global delay

    if inputs.is_pressed["Right"]: root.move_object(img, 0.2, 0)
    if inputs.is_pressed["Left"]: root.move_object(img, -0.2, 0)
    if inputs.is_pressed["Up"]: root.move_object(img, 0, -0.2)
    if inputs.is_pressed["Down"]: root.move_object(img, 0, 0.2)

    #if inputs.is_pressed["w"]: delay += 0.05
    #if inputs.is_pressed["s"]: delay -= 0.05

    root.update_func_misec(update_loop, 1)

def animation_update():

    anim_min_scr.play_anim_loop()
    anim_max_scr.play_anim_once()

    if root.window.fullScreenState == True:
        root.canvas.itemconfig(img, image=anim_max_scr.get_current_image())
        # if p_full != None:
            # timer += step
            # if timer >= delay:
                # timer = 0.0
                
                # root.canvas.itemconfig(img, image=p_full.image)
                
                # p_full = p_full.nextFrame
        # else:
            # p_full = anim_full_scr._Start
    else:
        root.canvas.itemconfig(img, image=anim_min_scr.get_current_image())
        # if p_min != None:
            # timer += step
            # if timer >= delay:
                # timer = 0.0
                
                # root.canvas.itemconfig(img, image=p_min.image)
                
                # p_min = p_min.nextFrame
        # else:
            # p_min = anim_min_scr._Start

    root.update_func_misec(animation_update, 1)

# Create threads for function1 and function2
thread1 = th.Thread(target=update_loop)
thread2 = th.Thread(target=animation_update)

# Start the threads
thread1.start()
thread2.start()

root.start_gameloop()

