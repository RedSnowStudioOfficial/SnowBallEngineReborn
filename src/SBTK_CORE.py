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

from .modules.sprite import SBTK_Sprite as sbtksprite

from .modules.game_window import SBTK_GameWindow as sbtkgamewindow

from .modules.containters.link_array import Link_Array as link_array

from PIL import Image, ImageTk, ImageFilter, PaletteFile

import threading as th

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
