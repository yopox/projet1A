import numpy as np
from gpiozero import Button

class Util:
    DIRS = ['UP', 'RIGHT', 'DOWN', 'LEFT']
    MOVE = {"UP": np.array([0, -1]),
            "RIGHT": np.array([1, 0]),
            "DOWN": np.array([0, 1]),
            "LEFT": np.array([-1, 0])}
    RIGHT = {'UP': 'RIGHT', 'RIGHT': 'DOWN', 'DOWN': 'LEFT', 'LEFT': 'UP'}
    LEFT = {'UP': 'LEFT', 'LEFT': 'DOWN', 'DOWN': 'RIGHT', 'RIGHT': 'UP'}
    P_BLOC = 80
    P_NONE = 35
    P1_LEFT = Button(19)
    P1_RIGHT = Button(21)
    P2_LEFT = Button(5)
    P2_RIGHT = Button(1)
    GAME_STATE = "GAME"

