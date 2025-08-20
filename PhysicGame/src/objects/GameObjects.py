import tkinter as tk
import math
from ..Settings import *
from ..algorithms.GameAlgorithms import *

class GameObject:
    def __init__(self, canva : tk.Canvas, pos_x : float = 0.0, pos_y : float = 0.0, name_tag : str = "origin", color : str = "white"):
        self.canva = canva

        self.name_tag = name_tag

        self.color = color

        self.parent : object = None
        self.childs : list = []

        self.pos = {"x":pos_x, "y":pos_y}

        self.ORIGIN : object = None

        self.get_object : list = []

    def add_child(self, child : object, pos_x_offcet: float = 0.0, pos_y_offcet: float = 0.0):
        if child.parent is not None:
            # Удаляем объект из списка детей старого родителя
            child.parent.childs.remove(child)
        child.parent = self
        child.pos["x"] = self.pos["x"] + pos_x_offcet
        child.pos["y"] = self.pos["y"] + pos_y_offcet
        
        #self.get_object.extend(child.get_object)
        self.childs.append(child)

    def remove_child(self, child : object):
        """Удаляет дочерний объект."""
        if child in self.childs:
            self.childs.remove(child)
            child.parent = None

    def draw_in(self):
        #для теста, далее всё будет зависеть от переключателя DEBUG в настройках игры*

        if self.parent == None:

            if IS_DUBUG:

                self.ORIGIN = self.canva.create_oval(self.pos["x"] - 1, self.pos["y"] - 1,
                                                    self.pos["x"] + 1, self.pos["y"] + 1,
                                                    fill="white", outline="")

            else:
                self.ORIGIN = self.canva.create_oval(self.pos["x"] - 1, self.pos["y"] - 1,
                                                    self.pos["x"] + 1, self.pos["y"] + 1,
                                                    fill="", outline="")

            self.canva.addtag_withtag("origin", self.ORIGIN)
            self.get_object.append(self.ORIGIN)

        if self.childs != None:
            for child in self.childs:
                child.draw_in()

    def clear_out(self):
        for i in self.get_object:
            self.canva.delete(i)

class SegmentObject(GameObject):
    def __init__(self, canva: tk.Canvas, pos_x: float = 0.0, pos_y: float = 0.0, 
                                         dir_x: float = 0.0, dir_y: float = 0.0, 
                                         name_tag : str = "segment", color: str = "red"):
        
        super().__init__(canva, pos_x, pos_y, name_tag, color)

        self.dir = {"x":dir_x, "y":dir_y}

        self.SEGMENT : object = None

    def draw_in(self):
        
        if IS_DUBUG:
            self.SEGMENT = self.canva.create_line(self.pos["x"], self.pos["y"], 
                                                self.pos["x"] + self.dir["x"], 
                                                self.pos["y"] + self.dir["y"], fill=self.color)
        else:
            self.SEGMENT = self.canva.create_line(self.pos["x"], self.pos["y"], 
                                                self.pos["x"] + self.dir["x"], 
                                                self.pos["y"] + self.dir["y"], fill="")
        
        if self.parent == None:
            self.get_object.append(self.SEGMENT)
        else:
           self.parent.get_object.append(self.SEGMENT)

        self.canva.addtag_withtag(self.name_tag, self.SEGMENT)

        return super().draw_in()

class RectangleObject(GameObject):
    def __init__(self, canva: tk.Canvas, pos_x: float = 0, pos_y: float = 0, width_rad : float = 10.0, height_rad : float = 10.0, name_tag : str = "rectangle", color : str = "white"):
        super().__init__(canva, pos_x, pos_y, name_tag, color)

        self.radius = {"width" : width_rad, "height" : height_rad}

        self.RECTANGLE : object = None

    def draw_in(self):

        if IS_DUBUG:
            self.RECTANGLE = self.canva.create_rectangle(self.pos["x"] - self.radius["width"], self.pos["y"] - self.radius["height"],
                                                         self.pos["x"] + self.radius["width"], self.pos["y"] + self.radius["height"],
                                                         fill=self.color, outline="")
        else:
            self.RECTANGLE = self.canva.create_rectangle(self.pos["x"] - self.radius["width"], self.pos["y"] - self.radius["height"],
                                                         self.pos["x"] + self.radius["width"], self.pos["y"] + self.radius["height"],
                                                         fill="", outline="")    
        
        if self.parent == None:
            self.get_object.append(self.RECTANGLE)
        else:
           self.parent.get_object.append(self.RECTANGLE)

        self.canva.addtag_withtag(self.name_tag, self.RECTANGLE)

        return super().draw_in()
    
class PlayerObject(GameObject):
    def __init__(self, canva: tk.Canvas, inputs : object, pos_x: float = 0, pos_y: float = 0, name_tag : str = "origin", color : str = "white"):
        super().__init__(canva, pos_x, pos_y, name_tag, color)
        
        self.sprite = None
        
        self.curr_layer = "Y_floor"
        
        self.get_input = inputs
        
        self.input_dir : dict = {"x" : 0.0,
                                 "y" : 0.0}
        
        self.SPD : dict = {"x" : 0.0,
                           "y" : 0.0}
        
        self.FLOOR_SPD : float = 0
        
        #Хитбокс игрока
        self.HITBOX = RectangleObject(canva, name_tag="hitbox", width_rad=9, height_rad=19, color="yellow")
        self.add_child(self.HITBOX)

        #Сенсоры пола
        self.LEFT_FLOOR_SENSOR = SegmentObject(canva, name_tag="left_floor_sensor", dir_x=0, dir_y=32, color="green")
        self.RIGHT_FLOOR_SENSOR = SegmentObject(canva, name_tag="right_floor_sensor", dir_x=0, dir_y=32, color="green")
        self.add_child(self.LEFT_FLOOR_SENSOR, -10)
        #self.add_child(self.RIGHT_FLOOR_SENSOR, 10)

        #Сенсоры потолка
        self.LEFT_CILING_SENSOR = SegmentObject(canva, name_tag="left_ciling_sensor", dir_x=0, dir_y=-32, color="blue")
        self.RIGHT_CILING_SENSOR = SegmentObject(canva, name_tag="right_ciling_sensor", dir_x=0, dir_y=-32, color="blue")
        #self.add_child(self.LEFT_CILING_SENSOR, -10)
        #self.add_child(self.RIGHT_CILING_SENSOR, 10)

        #Сенсоры Стен
        self.LEFT_WALL_SENSOR = SegmentObject(canva, name_tag="left_wall_sensor", dir_x=-10, dir_y=0, color="purple")
        self.RIGHT_WALL_SENSOR = SegmentObject(canva, name_tag="right_wall_sensor", dir_x=10, dir_y=0, color="purple")
        #self.add_child(self.LEFT_WALL_SENSOR)
        #self.add_child(self.RIGHT_WALL_SENSOR)
        
        #Сенсор Балансировки
        #self.BALANCE_CHECK_SENSOR = SegmentObject(canva, "balance_check_sensor", dir_x=0, dir_y=32, color="red")
        #self.add_child(self.BALANCE_CHECK_SENSOR)

        
        self.player_mode = None
        
        self.is_rolling : bool = False
        self.is_jumped : bool = False
        self.is_balancing : bool = False
        self.is_crouching : bool = False
        self.is_looking_up : bool = False

    def get_floor_info(self):
        left_overlap = None
        right_overlap = None

        left_distance = None
        right_distance = None

        left_angle = None
        right_angle = None

        left_tagid = None
        right_tagid = None

        left_overlap = get_overlap(self.canva, self.LEFT_FLOOR_SENSOR.SEGMENT)
        #right_overlap = get_overlap(self.canva, self.RIGHT_FLOOR_SENSOR.SEGMENT)

        for index, links in enumerate(left_overlap):
            point_cross = get_cross(self.canva, self.LEFT_FLOOR_SENSOR.SEGMENT, left_overlap[index])

            if point_cross != None:
                left_tagid = left_overlap[index]
                left_distance = get_distance(self.canva, self.LEFT_FLOOR_SENSOR.SEGMENT, point_cross)
                left_angle = get_angle(self.canva, self.LEFT_FLOOR_SENSOR.SEGMENT)
            
        #for index, links in enumerate(right_overlap):
        #    point_cross = get_cross(self.canva, self.RIGHT_FLOOR_SENSOR.SEGMENT, right_overlap[index])
#
        #    if point_cross != None:
        #        right_tagid = right_overlap[index]
        #        right_distance = get_distance(self.canva, self.RIGHT_FLOOR_SENSOR.SEGMENT, point_cross)
        #        right_angle = get_angle(self.canva, self.RIGHT_FLOOR_SENSOR.SEGMENT)
        
        return left_tagid, left_distance, left_angle
        #if left_distance != None and right_distance == None:
        #            return left_tagid, left_distance, left_angle #, "l_floor"
                
        #elif left_distance == None and right_distance != None:
        #            return right_tagid, right_distance, right_angle #, "r_floor"