import numpy as np
from util import Util


class Player():

    def __init__(self, c1, c2, c3, y_offset, tilemap):
        self.POS = np.array(
            [np.random.randint(0, 32), y_offset + np.random.randint(0, 15)])
        self.COLOR = [c1, c2, c3]
        tilemap[self.POS[0]][self.POS[1]].player = self
        global DIRS
        self.DIR = Util.DIRS[np.random.randint(0, 4)]
        self.LAST = "BLOC"

    def update(self, tilemap, over):
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
            over = True

    def smartMove(self, tilemap):
        intent = ""
        if np.random.randint(0, 2) == 0:
            intent = Util.LEFT[self.DIR]
        else:
            intent = Util.RIGHT[self.DIR]
        newPos = (self.POS + Util.MOVE[intent]) % 32
        if tilemap[newPos[0]][newPos[1]].player is None:
            self.DIR = intent
            self.LAST = "TURN"
