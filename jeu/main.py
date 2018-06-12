""" main.py
Fichier principal
"""

import time
import os
import sys
import numpy as np
from timer import Timer
from samplebase import SampleBase

DIRS = ['UP', 'RIGHT', 'DOWN', 'LEFT']
MOVE = {"UP" : np.array([0, -1]),
       "RIGHT" : np.array([1, 0]),
       "DOWN" : np.array([0, 1]),
       "LEFT" : np.array([-1, 0])}
RIGHT = {'UP' : 'RIGHT', 'RIGHT' : 'DOWN', 'DOWN' : 'LEFT', 'LEFT' : 'UP'}
LEFT = {'UP' : 'LEFT', 'LEFT' : 'DOWN', 'DOWN' : 'RIGHT', 'RIGHT' : 'UP'}
OVER = False

class Tile():

    def __init__(self, y, x):
        self.player = None
        self.x = x
        self.y = y

    def paint(self, screen):
        if self.player:
            screen.SetPixel(self.y, self.x, self.player.COLOR[0], self.player.COLOR[1], self.player.COLOR[2])

class Player():

    def __init__(self, c1, c2, c3, y_offset, map):
        self.POS = np.array([np.random.randint(0, 32), y_offset + np.random.randint(0,15)])
        self.COLOR = [c1, c2, c3]
        map[self.POS[0]][self.POS[1]].player = self
        global DIRS
        self.DIR = DIRS[np.random.randint(0,4)]
        self.LAST = "BLOC"
    def update(self, map):
        global MOVE, OVER
        self.POS += MOVE[self.DIR]
        self.POS = self.POS % 32
        tile = map[self.POS[0]][self.POS[1]]

        # Empty tile : the player moves
        if tile.player == None:
            if self.LAST == "TURN" or (self.LAST == "BLOC" and np.random.randint(0,100) <= 80) or (self.LAST == "NONE" and np.random.randint(0, 100) > 35):
                self.LAST = "BLOC"
                map[self.POS[0]][self.POS[1]].player = self
            else:
                self.LAST = "NONE"
        # Non empty tile : GAME OVER
        else:
            OVER = True

    def smartMove(self, map):
        global LEFT, RIGHT, MOVE
        intent = ""
        if np.random.randint(0, 2) == 0:
            intent = LEFT[self.DIR]
        else:
            intent = RIGHT[self.DIR]
        newPos = (self.POS + MOVE[intent]) % 32
        if map[newPos[0]][newPos[1]].player is None:
            self.DIR = intent
            self.LAST = "TURN"

class Snake(SampleBase):

    def __init__(self, *args, **kwargs):
        super(Snake, self).__init__(*args, **kwargs)

	# Init screen
        self.SIZE = 32

	# Init tilemap
        self.MAP = [[Tile(i, j) for j in range(32)] for i in range(32)]
        self.PLAYERS = [Player(10, 200, 10, 0, self.MAP),
                        Player(200, 10, 10, 17, self.MAP)]
        self.TIMER = Timer(6)

    def run(self):
        global OVER
        screen = self.matrix.CreateFrameCanvas()

        while not OVER:

	    # Fake inputs
            global LEFT, RIGHT
            if np.random.randint(0, 5) == 0:
                self.PLAYERS[0].smartMove(self.MAP)
            if np.random.randint(0, 6) == 0:
                self.PLAYERS[1].smartMove(self.MAP)

	    # Update pos
            self.PLAYERS[0].update(self.MAP)
            self.PLAYERS[1].update(self.MAP)

            # Draw map
            for line in self.MAP:
                for tile in line:
                    tile.paint(screen)

            # Wait and clear screen
            self.TIMER.tick()
            screen = self.matrix.SwapOnVSync(screen)

# Main function
if __name__ == "__main__":
    snake = Snake()
    if not snake.process():
        snake.print_help()
