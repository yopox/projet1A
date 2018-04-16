""" main.py
Fichier principal
"""

import time
import os
import sys
import numpy as np
from timer import Timer

SIZE = 32
MAP = [[0 for j in range(32)] for i in range(32)]
MAP[5][1] = 1
DIR = np.array([0, 1])
POS = np.array([5, 1])
TIMER = Timer(4)
SPRITES = ["#", "1"]
FRAME = 0


def draw():
    os.system('clear')
    for i in range(32):
        for j in range(32):
            print(SPRITES[MAP[i][j]], end="")
        print("")


while True:
    FRAME += 1
    if FRAME == 8:
        DIR[0] = 1
        DIR[1] = 0
    TIMER.tick()
    POS += DIR
    POS[0] = POS[0] % 32
    POS[1] = POS[1] % 32
    MAP[POS[0]][POS[1]] = 1
    draw()
