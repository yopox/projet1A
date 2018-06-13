import numpy as np
from util import Util


class Player():

    def __init__(self, c1, c2, c3, y_offset, tilemap):
        self.POS = np.array(
            [np.random.randint(0, 32), y_offset + np.random.randint(0, 15)])
        self.COLOR = [c1, c2, c3]
        tilemap[self.POS[0]][self.POS[1]].player = self
        self.DIR = Util.DIRS[np.random.randint(0, 4)]
        self.LAST = "BLOC"
        self.TURNED_LAST = False

    def update(self, tilemap):
        self.POS += Util.MOVE[self.DIR]
        self.POS = self.POS % 32
        tile = tilemap[self.POS[0]][self.POS[1]]

        # Empty tile : the player moves
        if tile.player is None:
            t = self.LAST == "TURN"
            b = self.LAST == "BLOC" and np.random.randint(
                0, 100) <= Util.P_BLOC
            n = self.LAST == "NONE" and np.random.randint(0, 100) > Util.P_NONE
            if t or b or n:
                self.LAST = "BLOC"
                tilemap[self.POS[0]][self.POS[1]].player = self
            else:
                self.LAST = "NONE"
        # Non empty tile : GAME OVER
        else:
            Util.GAME_STATE = "OVER"

    def input(self, left, right):
        if not self.TURNED_LAST:
            if left.is_pressed and not right.is_pressed:
                self.DIR = Util.LEFT[self.DIR]
                self.LAST = "TURN"
                self.TURNED_LAST = True
            if right.is_pressed and not left.is_pressed:
                self.DIR = Util.RIGHT[self.DIR]
                self.LAST = "TURN"
                self.TURNED_LAST = True
        else:
            self.TURNED_LAST = False
