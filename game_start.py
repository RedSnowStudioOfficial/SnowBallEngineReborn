from src.SBTK_CORE import *
from PhysicGame.src.GameCore import *

root = sbtkgamewindow(win_name=game_name, width=screen_size["width"], height=screen_size["height"], win_bg="blue")

inputs = sbtkinput(root.window, 
                    keys_binds["act_jump"], 
                    keys_binds["act_accept"],
                    keys_binds["act_back"],
                    keys_binds["act_special"],
                    keys_binds["act_left"],
                    keys_binds["act_right"],
                    keys_binds["act_up"],
                    keys_binds["act_down"])

player = PlayerObject(root.canvas, inputs, 100, 100)
player.draw_in()



root.canvas.create_line(0,200, 100, 200, fill="yellow")
root.canvas.create_line(100,200, 200, 150, fill="yellow")

def game_loop():
    
    #print(player.get_floor_info())

    root.update_func_misec(game_loop, 1)

game_loop()

root.start_gameloop()