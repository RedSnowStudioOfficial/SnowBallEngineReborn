import tkinter as tk
import math
from ..Settings import *
from ..algorithms.GameAlgorithms import *

class GameObject:
    def __init__(self, canva : tk.Canvas, pos_x : float = 0.0, pos_y : float = 0.0):
        self.canva = canva

        self.parent : object = None
        self.childs : list = []

        self.pos = [pos_x, pos_y]

        self.ORIGIN : object = None

        self.get_object : list = []

    def add_child(self, child : object, pos_x_offcet: float = 0.0, pos_y_offcet: float = 0.0):
        if child.parent is not None:
            # Удаляем объект из списка детей старого родителя
            child.parent.childs.remove(child)
        child.parent = self
        child.pos[0] = self.pos[0] + pos_x_offcet
        child.pos[1] = self.pos[1] + pos_y_offcet
        
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

                self.ORIGIN = self.canva.create_oval(self.pos[0] - 1, self.pos[1] - 1,
                                                    self.pos[0] + 1, self.pos[1] + 1,
                                                    fill="white", outline="")

            else:
                self.ORIGIN = self.canva.create_oval(self.pos[0] - 1, self.pos[1] - 1,
                                                    self.pos[0] + 1, self.pos[1] + 1,
                                                    fill="", outline="")

            self.canva.addtag_withtag("origin", self.ORIGIN)
            self.get_object.append(self.ORIGIN)

        if self.childs != None:
            for child in self.childs:
                child.draw_in()

    def clear_out(self):
        for i in self.get_object:
            self.canva.delete(i)

class SensorObject(GameObject):
    def __init__(self, canva: tk.Canvas, name_tag : str = "sensor", pos_x: float = 0.0, pos_y: float = 0.0, 
                                         dir_x: float = 0.0, dir_y: float = 0.0, 
                                         color: str = "red"):
        
        super().__init__(canva, pos_x, pos_y)

        self.name_tag = name_tag

        self.dir = [dir_x, dir_y]

        self.SENSOR : object = None

        self.color = color

    def draw_in(self):
        
        if IS_DUBUG:
            self.SENSOR = self.canva.create_line(self.pos[0], self.pos[1], 
                                                self.pos[0] + self.dir[0], 
                                                self.pos[1] + self.dir[1], fill=self.color)
        else:
            self.SENSOR = self.canva.create_line(self.pos[0], self.pos[1], 
                                                self.pos[0] + self.dir[0], 
                                                self.pos[1] + self.dir[1], fill="")
        
        if self.parent == None:
            self.get_object.append(self.SENSOR)
        else:
           self.parent.get_object.append(self.SENSOR)

        self.canva.addtag_withtag(self.name_tag, self.SENSOR)

        return super().draw_in()

class PlayerObject(GameObject):
    def __init__(self, canva: tk.Canvas, pos_x: float = 0, pos_y: float = 0):
        super().__init__(canva, pos_x, pos_y)

        self.LEFT_FLOOR_SENSOR = SensorObject(canva, "left_floor_sensor", dir_x=0, dir_y=32, color="green")
        self.RIGHT_FLOOR_SENSOR = SensorObject(canva, "right_floor_sensor", dir_x=0, dir_y=32, color="green")
        
        self.add_child(self.LEFT_FLOOR_SENSOR, -10)
        self.add_child(self.RIGHT_FLOOR_SENSOR, 10)

    def get_floor_info(self):
        left_overlap = None
        right_overlap = None

        left_distance = None
        right_distance = None

        left_angle = None
        right_angle = None

        left_tagid = None
        right_tagid = None

        left_overlap = get_overlap(self.canva, self.LEFT_FLOOR_SENSOR.SENSOR)
        right_overlap = get_overlap(self.canva, self.RIGHT_FLOOR_SENSOR.SENSOR)

        for index, links in enumerate(left_overlap):
            point_cross = get_cross(self.canva, self.LEFT_FLOOR_SENSOR.SENSOR, left_overlap[index])

            if point_cross != None:
                left_tagid = left_overlap[index]
                left_distance = get_distance(self.canva, self.LEFT_FLOOR_SENSOR.SENSOR, point_cross)
                left_angle = get_angle(self.canva, self.LEFT_FLOOR_SENSOR.SENSOR)
            
        for index, links in enumerate(right_overlap):
            point_cross = get_cross(self.canva, self.RIGHT_FLOOR_SENSOR.SENSOR, right_overlap[index])

            if point_cross != None:
                right_tagid = right_overlap[index]
                right_distance = get_distance(self.canva, self.RIGHT_FLOOR_SENSOR.SENSOR, point_cross)
                right_angle = get_angle(self.canva, self.RIGHT_FLOOR_SENSOR.SENSOR)
        
        return left_tagid, left_distance, left_angle
        #if left_distance != None and right_distance == None:
        #            return left_tagid, left_distance, left_angle #, "l_floor"
                
        #elif left_distance == None and right_distance != None:
        #            return right_tagid, right_distance, right_angle #, "r_floor"