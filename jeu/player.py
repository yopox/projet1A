import numpy as np
from util import Util


class Player():
    """Classe définissant un joueur."""

    def __init__(self, c1, c2, c3, y_offset, tilemap):
        self.POS = np.array([16 - y_offset + np.random.randint(0, 16),
                             np.random.randint(0, 32)])
        self.COLOR = [c1, c2, c3]
        tilemap[self.POS[1]][self.POS[0]].player = self
        self.DIR = Util.DIRS[np.random.randint(0, 4)]
        self.LAST = "BLOC"
        self.TURNED_LAST = False

    def update(self, tilemap):
        """Appelé à chaque frame pour faire avancer le joueur."""

        # Calcul de la nouvelle position
        self.POS += Util.MOVE[self.DIR]
        self.POS = self.POS % 32
        tile = tilemap[self.POS[1]][self.POS[0]]

        # Case vide : le joueur bouge
        if tile.type == "EMPTY":
            # t, b, n : conditions pour laisser une trainée
            t = self.LAST == "TURN"
            b = self.LAST == "BLOC" and \
                np.random.randint(0, 100) <= Util.P_BLOC
            n = self.LAST == "NONE" and \
                np.random.randint(0, 100) > Util.P_NONE
            if t or b or n:
                self.LAST = "BLOC"
                tile.type = "PLAYER"
                tile.player = self
            else:
                self.LAST = "NONE"

        # Objet : gomme
        elif tile.type == "ERASER":
            # On efface la trainée du joueur
            for line in tilemap:
                for tile2 in line:
                    if tile2.type == "PLAYER" and tile2.player == self:
                        tile2.type = "EMPTY"
            tile.type = "PLAYER"
            tile.player = self

        # Objet : bombe
        elif tile.type == "BOMB":
            # On efface les tiles dans un carré de rayon 7
            for j in range(7):
                for i in range(7):
                    y = (j - 3 + tile.y) % 32
                    x = (i - 3 + tile.x) % 32
                    tilemap[y][x].type = "EMPTY"
            self.LAST = "TURN"

        # On se déplace sur la trainée d'un joueur : Game Over
        elif tile.type == "PLAYER":
            Util.GAME_STATE = "LOSE"
            Util.WIN_COLOR = [210 - self.COLOR[0], 10, 210 - self.COLOR[2]]
            Util.WIN_POS = [self.POS[0], self.POS[1]]
            Util.TICK = -128

    def input(self, left, right):
        """Vérifie si le joueur souhaite tourner."""
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
