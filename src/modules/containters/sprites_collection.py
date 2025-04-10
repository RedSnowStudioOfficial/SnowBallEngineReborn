import link_array as la
from PIL import ImageTk, Image

import tkinter as tk

class Sprite:
    
    def __init__(self, name, filter : str) -> None:
        '''
        FILTERTS:

        NEAREST: Ближайший сосед (Nearest Neighbor). Этот метод просто выбирает ближайший пиксель к новому положению и копирует его значение.
        
        BOX: Блочное ресэмплирование (Box Resampling). Этот метод использует среднее значение пикселей в блоке для определения нового значения.
        
        BILINEAR: Билинейное ресэмплирование (Bilinear Resampling). Этот метод использует линейную интерполяцию для определения нового значения.
        
        HAMMING: Ресэмплирование Хэмминга (Hamming Resampling). Этот метод использует функцию Хэмминга для определения нового значения.
       
        BICUBIC: Бикубическое ресэмплирование (Bicubic Resampling). Этот метод использует кубическую интерполяцию для определения нового значения.
        
        LANCZOS: Ресэмплирование Ланцоша (Lanczos Resampling). Этот метод использует функцию Ланцоша для определения нового значения. Этот метод является наиболее точным, но также является самым медленным.
        
        '''
        
        self.name = name
        self.filter = filter
        self.modified_image = None
        
        self.original_image = None

        self.curr_size = None

    def Add_Image_From_Path_Crop(self, path, x, y, width, height):
        if self.modified_image == None:
            img = Image.open(path)
            self.original_image = img.crop((x, y, x+width, y+height))
            self.modified_image = img.crop((x, y, x+width, y+height))
            self.curr_size = self.original_image.size
            '''
            match filter:
                case "NEAREST":
                    self.modified_image = self.modified_image.resize((self.curr_size[0], self.curr_size[1]), resample=Image.NEAREST)
                case "BOX":
                    self.modified_image = self.modified_image.resize((self.curr_size[0], self.curr_size[1]), resample=Image.BOX)
                case "BILINEAR":
                    self.modified_image = self.modified_image.resize((self.curr_size[0], self.curr_size[1]), resample=Image.BILINEAR)
                case "HAMMING":
                    self.modified_image = self.modified_image.resize((self.curr_size[0], self.curr_size[1]), resample=Image.HAMMING)
                case "BICUBIC":
                    self.modified_image = self.modified_image.resize((self.curr_size[0], self.curr_size[1]), resample=Image.BICUBIC)
                case "LANCZOS":
                    self.modified_image = self.modified_image.resize((self.curr_size[0], self.curr_size[1]), resample=Image.LANCZOS)
            '''
        else:
            print("У спрайта уже есть картинка")

    def Add_Image_From_Path(self, path):
        if self.modified_image == None:
            self.original_image = Image.open(path)
            self.modified_image = Image.open(path)
            self.curr_size = self.original_image.size

            match filter:
                case "NEAREST":
                    self.modified_image = self.modified_image.resize((self.curr_width[0], self.curr_width[1]), resample=Image.NEAREST)
                case "BOX":
                    self.modified_image = self.modified_image.resize((self.curr_width[0], self.curr_width[1]), resample=Image.BOX)
                case "BILINEAR":
                    self.modified_image = self.modified_image.resize((self.curr_width[0], self.curr_width[1]), resample=Image.BILINEAR)
                case "HAMMING":
                    self.modified_image = self.modified_image.resize((self.curr_width[0], self.curr_width[1]), resample=Image.HAMMING)
                case "BICUBIC":
                    self.modified_image = self.modified_image.resize((self.curr_width[0], self.curr_width[1]), resample=Image.BICUBIC)
                case "LANCZOS":
                    self.modified_image = self.modified_image.resize((self.curr_width[0], self.curr_width[1]), resample=Image.LANCZOS)

        else:
            print("У спрайта уже есть картинка")

    def Add_Image_From_Image(self, image):
        if self.modified_image == None:
            self.original_image = image
            self.modified_image = self.original_image.copy()
            self.curr_size = self.original_image.size
        else:
            print("У спрайта уже есть картинка")

    def Set_Color_To_Transperency(self, curr_color):
        if self.modified_image:
            width, height = self.original_image.size #Берём размеры оригинала

            img = self.original_image.copy()
            img = img.convert('RGBA') #Перекидываем картинку в переменную и добавляем оригиналу альфа канал
            
            img = img.resize((width, height), resample=Image.NEAREST) #Форматируем под пиксельпёрфект формат отображения

            for x in range(width): #Пробегаемся по пикселям и заменяем цвет что указывали на прозрачность
                for y in range(height):
                    pixel = img.getpixel((x, y))
                    if pixel == curr_color:
                        img.putpixel((x, y), (0, 0, 0, 0))  # RGBA(0, 0, 0, 0) - прозрачный пиксель
            
                match filter:
                    case "NEAREST":
                        img = img.resize((width, height), resample=Image.NEAREST)
                    case "BOX":
                        img = img.resize((width, height), resample=Image.BOX)
                    case "BILINEAR":
                        img = img.resize((width, height), resample=Image.BILINEAR)
                    case "HAMMING":
                        img = img.resize((width, height), resample=Image.HAMMING)
                    case "BICUBIC":
                        img = img.resize((width, height), resample=Image.BICUBIC)
                    case "LANCZOS":
                        img = img.resize((width, height), resample=Image.LANCZOS)
                
                self.modified_image = img

                self.img = None
        
        else:
            print("У спрайта нет картинки")

    def Set_Scale(self, value):
        
        if self.modified_image:
            width, height = self.modified_image.size
            new_width = int(width * value)
            new_height = int(height * value)
            self.curr_size[0] = new_width
            self.curr_size[1] = new_height
            match filter:
                case "NEAREST":
                    self.modified_image = self.modified_image.resize((new_width, new_height), resample=Image.NEAREST)
                case "BOX":
                    self.modified_image = self.modified_image.resize((new_width, new_height), resample=Image.BOX)
                case "BILINEAR":
                    self.modified_image = self.modified_image.resize((new_width, new_height), resample=Image.BILINEAR)
                case "HAMMING":
                    self.modified_image = self.modified_image.resize((new_width, new_height), resample=Image.HAMMING)
                case "BICUBIC":
                    self.modified_image = self.modified_image.resize((new_width, new_height), resample=Image.BICUBIC)
                case "LANCZOS":
                    self.modified_image = self.modified_image.resize((new_width, new_height), resample=Image.LANCZOS)

        else:
            print("У спрайта нет картинки")

    def Get_Rotated_Image(self, angle : float):
        match filter:
                case "NEAREST": 
                    return self.modified_image.rotate(angle=angle, resample=Image.NEAREST)
                case "BOX":
                    return self.modified_image.rotate(angle=angle, resample=Image.BOX)
                case "BILINEAR":
                    return self.modified_image.rotate(angle=angle, resample=Image.BILINEAR)
                case "HAMMING":
                    return self.modified_image.rotate(angle=angle, resample=Image.HAMMING)
                case "BICUBIC":
                    return self.modified_image.rotate(angle=angle, resample=Image.BICUBIC)
                case "LANCZOS":
                    return self.modified_image.rotate(angle=angle, resample=Image.LANCZOS)

    def Get_ImageTk(self):
        if self.modified_image:
            image_tk = ImageTk.PhotoImage(self.modified_image)
            return image_tk
        else:
            print("У спрайта нет картинки")
            return None

    def Get_ImagePill(self):
        if self.modified_image:
            return self.modified_image
        else:
            print("У спрайта нет картинки")
            return None

    def Get_Name(self):
        return self.name

class Sprites_Collection(la.Link_Array):
    
    def __init__(self):
        super().__init__()

    def Add_Sprite_From_Path_Crop(self, name, path, _filter, x, y, width, height):
        new_sprite = Sprite(name, _filter)
        new_sprite.Add_Image_From_Path_Crop(path, x, y, width, height)

        self.Add_In_End(new_sprite)

    def Add_Sprite_From_Path(self, name, path, _filter):
        new_sprite = Sprite(name, _filter)
        new_sprite.Add_Image_From_Path(path)
        
        self.Add_In_End(new_sprite)

    def Get_Rotation_Copy(self, angle : float):
        new_collection = Sprites_Collection()
        
        p = self._Start

        while p != None:
            new_sprite = Sprite(p.elem.name, p.elem.filter)
            new_sprite.original_image = p.elem.Get_Rotated_Image(angle)
            new_sprite.modified_image = new_sprite.original_image.copy()

            new_collection.Add_In_End(new_sprite)

            p = p.nextNode

if __name__ == "__main__":

    root = tk.Tk()

    canva = tk.Canvas(root, width=640, height=480, bg="black")
    canva.pack()

    sprites = Sprites_Collection()

    filter_ = "NEAREST"

    sprites.Add_Sprite_From_Path_Crop("stand", r"resources\images\Player_Sprites.png", filter_, 2, 2, 24, 32)
    sprites.Add_Sprite_From_Path_Crop("stand1", r"resources\images\Player_Sprites.png", filter_, 2, 40, 44, 32)
    sprites.Add_Sprite_From_Path_Crop("stand2", r"resources\images\Player_Sprites.png", filter_, 2, 2, 24, 32)
    sprites.Add_Sprite_From_Path_Crop("stand3", r"resources\images\Player_Sprites.png", filter_, 2, 2, 24, 32)
    sprites.Add_Sprite_From_Path_Crop("stand4", r"resources\images\Player_Sprites.png", filter_, 2, 2, 24, 32)

    canva.create_image(10, 10, image=sprites.Get_Elem_By_Position(0).Get_ImageTk())
    canva.create_line(10, 10, 100, 100, fill="red")

    #sprites.Get_Elem_By_Position(0).modified_image = sprites.Get_Elem_By_Position(0).modified_image.rotate(45, expand=True)

    #canva.itemconfig(canvaimg, image=sprites.Get_Elem_By_Position(0).Get_ImageTk())

    root.mainloop()