from .containters.link_array import Link_Array
from PIL import ImageTk, Image

import tkinter as tk

#Двойная ротация спрайта с использованием PILL вызывает визуальные артефакты
#Впрочем, спрайт будет сохраняться в файл, поэтому это никак не будет задействованно
#spr1.Set_Rotation(45)

class SBTK_Sprite:
    
    def __init__(self, name):
        self.name = name
        self.image = None
        self.imageTk = None

        self.resample_method = Image.NEAREST

        self.nextSprite = None
        self.prevSprite = None

    def Add_Image_From_Path(self, path):
        if self.image == None:
            self.image = Image.open(path)
            self.imageTk = ImageTk.PhotoImage(self.image)
        else:
            print("Уже есть связанная картинка")

    def Add_Image_From_Path_Crop(self, path, x, y, width, height):
        
        if self.image == None:
            img = Image.open(path)
            self.image = img.crop((x, y, x+width, y+height))
            self.imageTk = ImageTk.PhotoImage(self.image)
        else:
            print("Уже есть связанная картинка")

    def Add_Image_From_Image(self, image):
        if self.image == None:
            self.image = image
            self.imageTk = ImageTk.PhotoImage(self.image)
        else:
            print("Уже есть связанная картинка")

    def Set_Color_To_Color(self, get_color, set_color):
        
        if self.image == None:
            print("Нет картинки")
        else:
            width, height = self.image.size
            img = self.image.copy()
            img = img.convert("RGBA")

            for x in range(width):
                for y in range(height):
                    pixel = img.getpixel((x,y))
                    if pixel == get_color:
                        img.putpixel((x, y), set_color)
            
            self.image = img
            self.imageTk = ImageTk.PhotoImage(self.image)

    def Set_Scale(self, scale_x, scale_y):

        if self.image == None:
            print("Нет картинки")
        else:
            width, height = self.image.size
            new_width = int(width * scale_x)
            new_height = int(height * scale_y)
            self.image = self.image.resize((new_width, new_height), resample=self.resample_method)
            self.imageTk = ImageTk.PhotoImage(self.image)

    def Set_Rotation(self, rotation_degrees):
        if self.image == None:
            print("Нет картинки")
        else:
            self.image = self.image.rotate(rotation_degrees, expand=True, resample=self.resample_method)
            self.imageTk = ImageTk.PhotoImage(self.image)

    def Set_Flip_Horizontal(self):
        if self.image == None:
            print("Нет картинки")
        else:
            self.image = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            self.imageTk = ImageTk.PhotoImage(self.image)

    def Set_Flip_Vertical(self):
        if self.image == None:
            print("Нет картинки")
        else:
            self.image = self.image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            self.imageTk = ImageTk.PhotoImage(self.image)

    def Set_Resample(self, resample_method):
        self.resample_method = resample_method

    def Get_Rotated_Image(self, rotation_degrees):
        if self.image == None:
            print("Нет картинки")
            return None
        else:
            return self.image.rotate(rotation_degrees, expand=True, resample=self.resample_method)

    def Get_Scaled_Image(self, scale_x, scale_y):
        if self.image == None:
            print("Нет картинки")
            return None
        else:
            width, height = self.image.size
            new_width = int(width * scale_x)
            new_height = int(height * scale_y)
            return self.image.resize((new_width, new_height), resample=self.resample_method)

    def Get_Image(self):
        if self.image == None:
            print("Нет картинки")
        else:
            return self.image

    def Get_ImageTk(self):
        if self.image == None:
            print("Нет картинки")
            return None
        else:
            return self.imageTk

class SBTK_Sprite_Animation(Link_Array):
    
    def __init__(self, name, anim_step, frame_delay, anim_time):
        super().__init__()

        self.name = name
        self.anim_step = anim_step
        self.anim_time = anim_time
        self.frame_time = 0.0
        self.frame_delay = frame_delay
        self.curr_frame = None

    def Add_Frame_From_Image(self, path, frame_name, position):
        #Создаём экземпляр спрайта для нового кадра
        new_frame = SBTK_Sprite(frame_name)
        #Загружаем картинку в спрайт
        new_frame.Add_Image_From_Path(path)

        #Если в списке нет элементов
        if self._Start == None:
            self.Add_In_End(new_frame)
        else:
            if self.Get_Count_Elements() >= position:
                self.Add_In_End(new_frame)
            elif position == 0:
                self.Add_In_Start(new_frame)
            else:
                self.Add_In_Position(new_frame, position)

    def Add_Frame_From_Crop_Image(self, path, frame_name, x, y, width, height, position):
        #Создаём экземпляр спрайта для нового кадра
        new_frame = SBTK_Sprite(frame_name)
        #Загружаем картинку в спрайт
        new_frame.Add_Image_From_Path_Crop(path, x, y, width, height)
        
        #Если в списке нет элементов
        if self._Start == None:
            self.Add_In_End(new_frame)
        else:
            if self.Get_Count_Elements() >= position:
                self.Add_In_End(new_frame)
            elif position == 0:
                self.Add_In_Start(new_frame)
            else:
                self.Add_In_Position(new_frame, position)

    def Add_Frame_From_Sprite(self, sprite, position):
        
        new_frame = sprite

        #Если в списке нет элементов
        if self._Start == None:
            self.Add_In_End(new_frame)
        else:
            if self.Get_Count_Elements() >= position:
                self.Add_In_End(new_frame)
            elif position == 0:
                self.Add_In_Start(new_frame)
            else:
                self.Add_In_Position(new_frame, position)

    def Set_Anim_Spd(self, spd : float):
        self.anim_step = spd

    def Set_Anim_Time(self, time : float):
        self.anim_time = time

    def Play_Anim(self, is_looped:bool):
        p = self._Start
        
        if self._Start == None:
            print("Кадров нету")
        else:
            if is_looped == True:
                if p != None:
                    self.anim_time += self.anim_step
                    self.frame_time += self.anim_step
                    if self.frame_time >= self.frame_delay:
                        self.frame_time = 0.0
                        p = p.nextNode
                else:
                    p = self._Start

            if is_looped == False:
                if p != None:
                    self.frame_time += self.frame_delay
                    if self.frame_time >= self.frame_delay:
                        self.frame_time = 0.0
                        p = p.nextNode
                    else:
                        p = self._End

class SBTK_Animation_Tree(Link_Array):
    
    def __init__(self):
        super().__init__()
        pass