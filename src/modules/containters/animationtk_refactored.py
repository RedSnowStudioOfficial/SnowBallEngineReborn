from .link_array import Link_Array, Link_Node
import tkinter as tk

class FrameTK(Link_Node):
    def __init__(self, name):
        super().__init__(name)
        self.image = None

    def add_image_path(self, path):
        if self.image is None:
            self.image = tk.PhotoImage(file=path)
        else:
            print("Уже есть картинка")

    def add_image_path_crop(self, path, x, y, width, height):
        if self.image is None:
            crop_image = tk.PhotoImage(file=path)
            self.add_image_crop(crop_image, x, y, width, height)
        else:
            print("Уже есть картинка")

    def add_image(self, image):
        if self.image is None:
            self.image = tk.PhotoImage.copy(image)
        else:
            print("Уже есть картинка")

    def add_image_crop(self, image, x, y, width, height):
        if self.image is None:
            crop_image = tk.PhotoImage(width=width, height=height)

            for i in range(0, width):
                for j in range(0, height):
                    crop_image.put('#%02x%02x%02x' % image.get(x+i, y+j), to=(i, j))
                
            self.image = crop_image
        else:
            print("Уже есть картинка")

    def copy_image(self, frame):
        if frame.image is None:
            print("Нет картинки в объекте кадра")
        else:
            self.image = frame.image.copy()

    def copy_name(self, frame):
        if frame.name is None:
            print("Имя кадра не было задано")
        else:
            self.name = str(frame.name)

    def get_name(self):
        if self.elem is None:
            print("Имя не было задано")
        else:
            return str(self.elem)

    def get_scaled_frame(self, scale : int):
        if self.image is None:
            print("Нет картинки")
        else:
            if scale < 0:
                return self.image.subsample(scale, scale)
            elif scale > 0:
                return self.image.zoom(scale, scale)
            elif scale == 0:
                return self.image

    def get_image_with_changed_color(self, old_color, new_color):
        if self.image is None:
            print("Нет картинки")
        else:
            width, height = self.image.width(), self.image.height()
            new_image = self.image.copy()

            for x in range(width):
                for y in range(height):
                    if new_image.get(x, y) == old_color:
                        new_image.put('#%02x%02x%02x' % new_color, to=(x, y))
            
            return new_image

    def get_image_with_transperented_color(self, color):
        if self.image is None:
            print("Нет картинки")
        else:
            width, height = self.image.width(), self.image.height()
            new_image = self.image.copy()
            for x in range(width):
                for y in range(height):
                    if new_image.get(x, y) == color:
                        new_image.transparency_set(x, y, 1)
            
            return new_image

    def get_image_link(self):
        if self.image is None:
            print("Нет картинки")
        else:
            return self.image
    
    def get_image_copy(self):
        if self.image is None:
            print("Нет картинки")
        else:
            copy_image = self.image.copy()
            return copy_image

    def save_frame_as_image(self, path):
        self.image.write(path)

class AnimationTK(Link_Array):
    def __init__(self) -> None:
        super().__init__()

        self.step : float = 0.1
        self.delay : float = 10
        self.frame_time : float = 0.0

        self.animation_timer : float = 0.0

        self.play_loop : bool = True
        self.play_backward : bool = False

        self.p = self._Start

    def add_frame_end_path_crop(self, name, path, x, y, width, height):
        new_frame = FrameTK(name)
        new_frame.add_image_path_crop(path, x, y, width, height)
        self.Add_In_End(new_frame)

    def add_frame_end_path_image(self, name, path):
        new_frame = FrameTK(name)
        new_frame.add_image_path(path)
        self.Add_In_End(new_frame)

    def add_frame_end_crop(self, name, image, x, y, width, height):
        new_frame = FrameTK(name)
        new_frame.add_image_crop(image, x, y, width, height)
        self.Add_In_End(new_frame)

    def add_frame_end_image(self, name, image):
        new_frame = FrameTK(name)
        new_frame.add_image(image)
        self.Add_In_End(new_frame)

    def copy_animation(self, additional_name, animTK):
        if animTK._Start is None:
            print("Анимация не имеет кадров")
        else:
            j = animTK._Start

            for z in range(animTK.Get_Count_Elements()):
                if j is not None:
                    new_name = j.elem.get_name() + additional_name
                    new_image = j.elem.get_image_copy()
                    self.add_frame_end_image(new_name, new_image)
                    j = j.nextNode

            self.step = animTK.step
            self.delay = animTK.delay
            self.frame_time = animTK.frame_time

            self.animation_timer = animTK.animation_timer

            self.play_loop = animTK.play_loop
            self.play_backward = animTK.play_backward

    def set_all_frames_color(self, old_color, new_color):
        p = self._Start

        for i in range(self.get_count_frames()):
            p.elem.image = p.elem.get_image_with_changed_color(old_color, new_color)
            p = p.nextNode

    def set_all_frames_transperent_color(self, color):
        p = self._Start

        for i in range(self.get_count_frames()):
            p.elem.image = p.elem.get_image_with_transperented_color(color)
            p = p.nextNode

    def set_all_frames_pallete(self, palletes : tk.PhotoImage, old_pallete_y, new_pallete_y):
        if self._Start is not None:
            p = self._Start

            for x in range(palletes.width()):
                self.set_all_frames_color(palletes.get(x, old_pallete_y), palletes.get(x, new_pallete_y))
            
    def scale_all_frames(self, scale):
        if self._Start is not None:
            p = self._Start

            for i in range(self.get_count_frames()):
                p.elem.image = p.elem.get_scaled_frame(scale)
                p = p.nextNode

            print("DONE")

    def play_animation(self):
        if self.p is not None:
            self.frame_time += self.step
            if self.frame_time >= self.delay:
                self.frame_time = 0.0
                
                self.p = self.p.nextNode
                
        else:
            self.p = self._Start

    def get_count_frames(self):
        p = self._Start
        counter = 0

        while p is not None:
            counter += 1
            p = p.nextNode
            
        return counter

    def get_current_frame(self):
        if self.p is not None:
            return self.p.elem
    
    def get_current_image(self):
        if self.p is not None:
            return self.p.elem.get_image_link()

    def save_all_frames_as_images(self, path):
        p = self._Start

        for i in range(self.get_count_frames()):
            p.elem.save_frame_as_image(path + "\\" + p.elem.name + ".png")
            p = p.nextNode

class AnimationSwapTK(AnimationTK):
    def __init__(self):
        super().__init__()

    def add_animation_end(self, animTK : AnimationTK):
        if self._Start is None:
            self._Start = animTK
            self._End = animTK
        else:
            self._End.nextAnim = animTK
            self._End = animTK

    def get_current_animation(self):
        if self.p is not None:
            return self.p.elem

    def swap_animation(self):
        p = self._Start

        for i in range(self.get_count_frames()):
            p.elem.play_animation()
            p = p.nextAnim
