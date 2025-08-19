'''
Сюда будут подключатся все модули что будут в движке*
Тем самым подключив только CORE модуль мы сможем работать со всеми сразу*

Файлы ресурсов ускорят загрузку картинок и прочего?

Скролинг канвы или экрана?

Поворот картинок?

Приближение и отдаление канвы?
'''

from .modules.window import SBTK_Window as sbtkwindow
from .modules.canvas import SBTK_Canvas as sbtkcanva
from .modules.inputs import SBTK_Inputs as sbtkinput

#from .modules.spritePILL import 

from .modules.game_window import SBTK_GameWindow as sbtkgamewindow

from .modules.containters.link_array import Link_Node as link_node
from .modules.containters.link_array import Link_Array as link_array
from .modules.containters.hash import HashTable as hash_table
#from .modules.animation_collection import AnimationHashTable as animhash

from PIL import Image, ImageTk, ImageFilter, PaletteFile

from .modules.spriteTK import FrameTK as sbtkframe
from .modules.spriteTK import AnimationTK as sbtkanimation

import threading as thread
import subprocess as subprocess
import multiprocessing as multiprocess

import random
import math

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":

    #from должен быть подключён без точки для работы вне main файла

    Width = 320
    Height = 240

    #win_test = sbtkwindow("SBTK_CORE_TEST", Width, Height, False)

    #canva_test = sbtkcanva(win_test, width=Width, height=Height, bg="black")
    #input_test = sbtkinput(canva_test)
    
    gamewin_test = sbtkgamewindow()

    def main_update():

        gamewin_test.update_func_misec(main_update, 1)
        
    main_update()
    
    gamewin_test.start_gameloop()
