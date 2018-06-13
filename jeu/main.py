""" main.py
Fichier principal
"""

import numpy as np
import util
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
        self.players = [player.Player(10, 200, 10, 0, self.MAP),
                        player.Player(200, 10, 10, 17, self.MAP)]
        self.timer = Timer(6)
        self.over = False

    def run(self):
        screen = self.matrix.CreateFrameCanvas()

        while not self.over:

            # Fake inputs
            if np.random.randint(0, 5) == 0:
                self.players[0].smartMove(self.tilemap)
            if np.random.randint(0, 6) == 0:
                self.players[1].smartMove(self.tilemap)

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
