import numpy as np
from gpiozero import Button


class Util:
    DIRS = ['UP', 'RIGHT', 'DOWN', 'LEFT']
    MOVE = {"UP": np.array([0, -1]),
            "RIGHT": np.array([1, 0]),
            "DOWN": np.array([0, 1]),
            "LEFT": np.array([-1, 0])}
    LEFT = {'UP': 'RIGHT', 'RIGHT': 'DOWN', 'DOWN': 'LEFT', 'LEFT': 'UP'}
    RIGHT = {'UP': 'LEFT', 'LEFT': 'DOWN', 'DOWN': 'RIGHT', 'RIGHT': 'UP'}
    P_BLOC = 80
    P_NONE = 35
    P1_LEFT = Button(19)
    P1_RIGHT = Button(21)
    P2_LEFT = Button(5)
    P2_RIGHT = Button(1)
    GAME_STATE = "TITLE"
    KURVE = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 1], [2, 2], [2, 4],
             [4, 2], [4, 3], [4, 4], [5, 4], [6, 2], [6, 3], [6, 4],
             [8, 2], [8, 3], [8, 4], [9, 2],
             [11, 2], [12, 3], [13, 2], [13, 3], [13, 4],
             [15, 1], [15, 2], [15, 3], [16, 0], [16, 2], [16, 4], [17, 0], [17, 4]]
    GREY = [180, 180, 180]
    TICK = 0
    WIN_COLOR = [0, 0, 0]
    WIN_POS = [0, 0]
    ITEMS = ["ERASER", "BOMB"]
