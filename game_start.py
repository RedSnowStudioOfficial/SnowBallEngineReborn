from src.SBTK_CORE import *
from PhysicGame.src.GameCore import *

root = sbtkgamewindow(win_name=game_name, width=screen_size[0], height=screen_size[1], win_bg="blue")

player = PlayerObject(root.canvas, 0, 170)
player.draw_in()

root.canvas.create_line(0,200, 100, 200, fill="yellow")
root.canvas.create_line(100,200, 200, 150, fill="yellow")

def game_loop():

    for i in player.get_object:
        root.canvas.move_obj(i, 0.02, 0)
    
    print(player.get_floor_info())

    root.update_func_misec(game_loop, 1)

game_loop()

root.start_gameloop()