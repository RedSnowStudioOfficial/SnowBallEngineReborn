import tkinter as tk
from PIL import Image, ImageTk
import math

class FrameTK:
    def __init__(self):
        self.name = None
        self.image = None

        self.nextFrame = None
        self.prevFrame = None

    def set_name(self, name):
        if self.name == None:
            self.name = name

    def add_image_path(self, path):
        if self.image == None:
            self.image = tk.PhotoImage(file=path)
        else:
            print("Уже есть картинка")

    def add_image_path_crop(self, path, x, y, width, height):
        if self.image == None:
            crop_image = tk.PhotoImage(file=path)
            self.add_image_crop(crop_image, x, y, width, height)
        else:
            print("Уже есть картинка")

    def add_image(self, image):
        if self.image == None:
            self.image = tk.PhotoImage.copy(image)
        else:
            print("Уже есть картинка")

    def add_image_crop(self, image, x, y, width, height):
        if self.image == None:
            crop_image = tk.PhotoImage(width=width, height=height)

            for i in range(0, width):
                for j in range(0, height):
                    crop_image.put('#%02x%02x%02x' % image.get(x+i, y+j), to=(i, j))
                
            self.image = crop_image
        else:
            print("Уже есть картинка")

    def copy_image(self, frame):
        if frame.image == None:
            print("Нет картинки в объекте кадра")
        else:
            self.image = frame.image.copy()

    def copy_name(self, frame):
        if frame.name == None:
            print("Имя кадра не было задано")
        else:
            self.name = str(frame.name)

    def get_name(self):
        if self.name == None:
            print("Имя не было задано")
        else:
            return str(self.name)

    def get_scaled_image_TK(self, scale : int):
        if self.image == None:
            print("Нет картинки")
        else:
            if scale < 0:
                return self.image.subsample(scale, scale)
            elif scale > 0:
                return self.image.zoom(scale, scale)
            elif scale == 0:
                return self.image

    def get_image_with_changed_color(self, old_color, new_color):
        if self.image == None:
            print("Нет картинки")
        else:
            width, height = self.image.width(), self.image.height()
            new_image = self.image.copy()

            for x in range(width): #Берём параметр ширины и высоты и пробегаемся по всем пиксялям
                for y in range(height):
                    if new_image.get(x, y) == old_color:
                        new_image.put('#%02x%02x%02x' % new_color, to=(x, y))
            
            return new_image

    def get_image_with_transperented_color(self, color):
        if self.image == None:
            print("Нет картинки")
        else:
            width, height = self.image.width(), self.image.height()
            new_image = self.image.copy()
            #Удаление заднего слоя на прозрачность
            #Пробегаемся по пикселям картинки
            for x in range(width): #Берём параметр ширины и высоты и пробегаемся по всем пиксялям
                for y in range(height):
                    if new_image.get(x, y) == color:
                        new_image.transparency_set(x, y, 1)
            
            return new_image

    def get_rotated_90deg_to_right_image_TK(self):
        if self.image == None:
            print("Нет картинки")
        else:
            width, height = self.image.width(), self.image.height()
            new_image = tk.PhotoImage(height=width, width=height)

            for x in range(width): #Берём параметр ширины и высоты и пробегаемся по всем пиксялям
                for y in range(height):
                    new_image.put('#%02x%02x%02x' % self.image.get(x, y), to=(height-y, x))
            
            return new_image

    def get_rotated_90deg_to_left_imag_TK(self):
        if self.image == None:
            print("Нет картинки")
        else:
            width, height = self.image.width(), self.image.height()
            new_image = tk.PhotoImage(height=width, width=height)

            for x in range(width): #Берём параметр ширины и высоты и пробегаемся по всем пиксялям
                for y in range(height):
                    new_image.put('#%02x%02x%02x' % self.image.get(x, y), to=(y, width-x))
            
            return new_image

    def get_rotated_image_PIL2TK(self, angle_deg):
        pil_image = ImageTk.getimage(self.image)
        rotated = pil_image.rotate(angle_deg, expand=True, resample=Image.NEAREST)
        return ImageTk.PhotoImage(rotated)

    def get_scaled_image_PIL2TK(self, scale_x, scale_y):
        pil_image = ImageTk.getimage(self.image)
        width, height = pil_image.size
        new_width = int(width * scale_x)
        new_height = int(height * scale_y)
        scaled = pil_image.resize((new_width, new_height), resample=Image.NEAREST)
        return ImageTk.PhotoImage(scaled)

    def get_mirrored_horizontal_image(self):
        if self.image == None:
            print("Нет картинки")
        else:
            width, height = self.image.width(), self.image.height()
            new_image = self.image.copy()

            for x in range(width): #Берём параметр ширины и высоты и пробегаемся по всем пиксялям
                for y in range(height):
                    new_image.put('#%02x%02x%02x' % self.image.get(x, y), to=(width-x, y))
            
            return new_image

    def get_mirrored_vertical_image(self):
        if self.image == None:
            print("Нет картинки")
        else:
            width, height = self.image.width(), self.image.height()
            new_image = self.image.copy()

            for x in range(width): #Берём параметр ширины и высоты и пробегаемся по всем пиксялям
                for y in range(height):
                    new_image.put('#%02x%02x%02x' % self.image.get(x, y), to=(x, height-y))
            
            return new_image

    def get_image_link(self):
        if self.image == None:
            print("Нет картинки")
        else:
            return self.image
    
    def get_image_copy(self):
        if self.image == None:
            print("Нет картинки")
        else:
            copy_image = self.image.copy()
            return copy_image

    def save_frame_as_image(self, path):
        self.image.write(path)

class AnimationTK:
    def __init__(self):
        
        self.name = None

        self._Start = None
        self._End = None

        self.nextAnim = None
        self.prevAnim = None

        self.step : float = 0.1 #Шаг анимации
        self.delay : float = 10 #Промежуток между кадрами
        self.frame_time : float = 0.0 #Осноной таймер

        self.animation_timer : float = 0.0

        self.play_loop : bool = True
        self.play_backward : bool = False

        self.p = self._Start

    def set_name(self, name):
        if self.name == None:
            self.name = name

    def add_frame_end_path_crop(self, name, path, x, y, width, height):
        
        new_frame = FrameTK()
        new_frame.set_name(name)
        new_frame.add_image_path_crop(path, x, y, width, height)

        if self._Start == None:
            self._Start = new_frame
            self._End = new_frame
        else:
            self._End.nextFrame = new_frame
            self._End = new_frame

    def add_frame_end_path_image(self, name, path):
        
        new_frame = FrameTK()
        new_frame.set_name(name)
        new_frame.add_image_path(path)

        if self._Start == None:
            self._Start = new_frame
            self._End = new_frame
        else:
            self._End.nextFrame = new_frame
            self._End = new_frame

    def add_frame_end_crop(self, name, image, x, y, width, height):
        
        new_frame = FrameTK()
        new_frame.set_name(name)
        new_frame.add_image_crop(image, x, y, width, height)

        if self._Start == None:
            self._Start = new_frame
            self._End = new_frame
        else:
            self._End.nextFrame = new_frame
            self._End = new_frame

    def add_frame_end_image(self, name, image):
        
        new_frame = FrameTK()
        new_frame.set_name(name)
        new_frame.add_image(image)

        if self._Start == None:
            self._Start = new_frame
            self._End = new_frame
        else:
            self._End.nextFrame = new_frame
            self._End = new_frame

    def copy_animation(self, additional_name, animTK):
        if animTK._Start == None:
            print("Анимация не имеет кадров")
        else:
            j = animTK._Start

            for z in range(animTK.get_count_frames()):
                if j != None:
                    new_name = j.get_name() + additional_name
                    new_image = j.get_image_copy()
                    
                    self.add_frame_end_image(new_name, new_image)
                    j = j.nextFrame

            self.step = animTK.step
            self.delay = animTK.delay
            self.frame_time = animTK.frame_time

            self.animation_timer = animTK.animation_timer

            self.play_loop = animTK.play_loop
            self.play_backward = animTK.play_backward

    def set_all_frames_color(self, old_color, new_color):
        p = self._Start

        for i in range(self.get_count_frames()):
            p.image = p.get_image_with_changed_color(old_color, new_color)
            p = p.nextFrame

    def set_all_frames_transperent_color(self, color):
        p = self._Start

        for i in range(self.get_count_frames()):
            p.image = p.get_image_with_transperented_color(color)
            p = p.nextFrame

    def set_all_frames_pallete(self, palletes : tk.PhotoImage, old_pallete_y, new_pallete_y):
        #Пробегается по картинке палитры и заменяет выбранный слой по горизонтали на тот что будет выбран вторым
        if self._Start != None:
            p = self._Start

            for x in range(palletes.width()):
                self.set_all_frames_color(palletes.get(x, old_pallete_y), palletes.get(x, new_pallete_y))
                p.nextFrame
    
    def scale_all_frames_PILL2TK(self, scale_x, scale_y):
            if self._Start != None:
                p = self._Start

                for i in range(self.get_count_frames()):
                    p.image = p.get_scaled_image_PIL2TK(scale_x, scale_y)
                    p = p.nextFrame

                print("DONE")

    def scale_all_frames(self, scale):
        if self._Start != None:
            p = self._Start

            for i in range(self.get_count_frames()):
                p.image = p.get_scaled_image_TK(scale)
                p = p.nextFrame

            print("DONE")

    def rotate_all_frames_PILL2TK(self, angle_deg):
        if self._Start != None:
            p = self._Start

            for i in range(self.get_count_frames()):
                p.image = p.get_rotated_image_PIL2TK(angle_deg)
                p = p.nextFrame

            print("DONE")

    def rotate_all_frames_90deg_to_right(self):
        if self._Start != None:
            p = self._Start

            for i in range(self.get_count_frames()):
                p.image = p.get_rotated_90deg_to_right_image()
                p = p.nextFrame

            print("DONE")
    
    def rotate_all_frames_90deg_to_left(self):
        if self._Start != None:
            p = self._Start

            for i in range(self.get_count_frames()):
                p.image = p.get_rotated_90deg_to_left_image()
                p = p.nextFrame

            print("DONE")
    
    def mirrored_all_frames_horizontal(self):
        if self._Start != None:
            p = self._Start

            for i in range(self.get_count_frames()):
                p.image = p.get_mirrored_horizontal_image()
                p = p.nextFrame

            print("DONE")
    
    def mirrored_all_frames_vertical(self):
        if self._Start != None:
            p = self._Start

            for i in range(self.get_count_frames()):
                p.image = p.get_mirrored_vertical_image()
                p = p.nextFrame

            print("DONE")

    def play_animation(self):
        if self.p != None:
            self.frame_time += self.step
            if self.frame_time >= self.delay:
                self.frame_time = 0.0
                
                self.p = self.p.nextFrame
                
        else:
            self.p = self._Start

    def get_count_frames(self):
        p = self._Start
        counter = 0

        while p != None:
            counter = counter + 1
            p = p.nextFrame

        return counter

    def get_current_frame(self):
        if self.p != None:
            return self.p
    
    def get_current_image(self):
        if self.p != None:
            return self.p.get_image_link()

    def save_all_frames_as_images(self, path):
        p = self._Start

        for i in range(self.get_count_frames()):
            p.save_frame_as_image(path + "\\" + p.name + ".png")
            p = p.nextFrame