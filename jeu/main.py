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
        self.type = "EMPTY"
        self.player = None
        self.x = x
        self.y = y

    def paint(self, screen):
        if self.type == "PLAYER":
            p = self.player
            screen.SetPixel(self.y, self.x, p.COLOR[0], p.COLOR[1], p.COLOR[2])


class Snake(SampleBase):

    def __init__(self, *args, **kwargs):
        super(Snake, self).__init__(*args, **kwargs)

        # Init tilemap
        self.tilemap = [[Tile(i, j) for j in range(32)] for i in range(32)]
        self.players = [player.Player(10, 10, 200, 0, self.tilemap),
                        player.Player(200, 10, 10, 17, self.tilemap)]
        self.timer = Timer(20)

    def run(self):
        screen = self.matrix.CreateFrameCanvas()

        while True:

            if Util.GAME_STATE == "TITLE":
                for pixel in Util.KURVE:
                    screen.SetPixel(pixel[1], pixel.[0],
                                    Util.GREY[0], Util.GREY[1], Util.GREY[2])
                for i in range(20):
                    self.timer.tick()

                if Util.P1_LEFT.is_pressed and Util.P1_RIGHT.is_pressed \
                        and Util.P2_LEFT.is_pressed and Util.P2_RIGHT.is_pressed:
                    screen.Clear()
                    Util.GAME_STATE = "GAME"

            if Util.GAME_STATE == "GAME":
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
                for i in range(4):
                    self.timer.tick()
                screen = self.matrix.SwapOnVSync(screen)

            if Util.GAME_STATE == "LOSE":
                for i in range(16):
                    self.timer.tick()


# Main function
if __name__ == "__main__":
    snake = Snake()
    if not snake.process():
        snake.print_help()
