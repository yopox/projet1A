""" main.py
Fichier principal
"""

import numpy as np
from util import Util
import player
from timer import Timer
from samplebase import SampleBase


class Tile():

    def __init__(self, y, x):
        self.player = None
        self.x = x
        self.y = y

    def paint(self, screen):
        if self.player:
            screen.SetPixel(
                self.y, self.x, self.player.COLOR[0], self.player.COLOR[1], self.player.COLOR[2])


class Snake(SampleBase):

    def __init__(self, *args, **kwargs):
        super(Snake, self).__init__(*args, **kwargs)

        # Init tilemap
        self.tilemap = [[Tile(i, j) for j in range(32)] for i in range(32)]
        self.players = [player.Player(10, 200, 10, 0, self.tilemap),
                        player.Player(200, 10, 10, 17, self.tilemap)]
        self.timer = Timer(6)
        self.state = "GAME"

    def run(self):
        screen = self.matrix.CreateFrameCanvas()

        while Util.GAME_STATE == "GAME":

            # Inputs
            self.players[0].input(Util.P1_LEFT, Util.P1_RIGHT)
            self.players[1].input(Util.P2_LEFT, Util.P2_RIGHT)

            # Update pos
            self.players[0].update(self.tilemap)
            self.players[1].update(self.tilemap)

            # Draw tilemap
            for line in self.tilemap:
                for tile in line:
                    tile.paint(screen)

            # Wait and clear screen
            self.timer.tick()
            screen = self.matrix.SwapOnVSync(screen)


# Main function
if __name__ == "__main__":
    snake = Snake()
    if not snake.process():
        snake.print_help()
