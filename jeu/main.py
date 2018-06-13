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
        elif self.type == "ERASER":
            screen.SetPixel(self.y, self.x, 200, 200, 200)
        elif self.type == "BOMB":
            screen.SetPixel(self.y, self.x, 227, 119, 25)
        else:
            screen.SetPixel(self.y, self.x, 0, 0, 0)

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
                screen.Clear()
                for pixel in Util.KURVE:
                    screen.SetPixel(7 + pixel[0], 18 + pixel[1],
                                    Util.GREY[0], Util.GREY[1], Util.GREY[2])
                    screen.SetPixel(24 - pixel[0], 13 - pixel[1],
                                    Util.GREY[0], Util.GREY[1], Util.GREY[2])

                screen = self.matrix.SwapOnVSync(screen)

                if Util.P1_LEFT.is_pressed and Util.P2_LEFT.is_pressed:
                    Util.GAME_STATE = "GAMETRANSITION"

                self.timer.tick()

            if Util.GAME_STATE == "GAMETRANSITION":
                for pixel in Util.KURVE:
                    a = 10 * Util.TICK
                    screen.SetPixel(7 + pixel[0], 18 + pixel[1],
                                    - a + Util.GREY[0], - a + Util.GREY[1], - a + Util.GREY[2])
                    screen.SetPixel(24 - pixel[0], 13 - pixel[1],
                                    - a + Util.GREY[0], - a + Util.GREY[1], - a + Util.GREY[2])

                Util.TICK += 1

                if Util.TICK == 18:
                    Util.TICK = 0
                    Util.GAME_STATE = "GAME"
                    self.players[1].DIR = "RIGHT"
                    self.players[0].DIR = "LEFT"
                    self.players[1].POS = np.array([-1 + np.random.randint(0, 16), np.random.randint(0, 32)])
                    self.players[0].POS = np.array([16 + np.random.randint(0, 16), np.random.randint(0, 32)])


                self.timer.tick()
                screen = self.matrix.SwapOnVSync(screen)



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

                # Spawn items
                if np.random.randint(0, 100) < 4:
                    x = np.random.randint(0, 32)
                    y = np.random.randint(0, 32)
                    while self.tilemap[y][x].type != "EMPTY":
                        x = np.random.randint(0, 32)
                        y = np.random.randint(0, 32)
                    self.tilemap[y][x].type = Util.ITEMS[np.random.randint(0, len(Util.ITEMS))]
                # Wait and clear screen
                for i in range(4):
                    self.timer.tick()
                screen = self.matrix.SwapOnVSync(screen)

            if Util.GAME_STATE == "LOSE":
                if Util.TICK >= -64:
                    screen.Clear()
                    for j in range(32):
                        for i in range(32):
                            dist = np.abs(j - Util.WIN_POS[1]) + np.abs(i - Util.WIN_POS[0])
                            if dist <= Util.TICK % 64 and Util.TICK < -64:
                                screen.SetPixel(j, i, 0, 0, 0)
                    for pixel in Util.KURVE:
                        screen.SetPixel(7 + pixel[0], 18 + pixel[1],
                                        Util.GREY[0], Util.GREY[1], Util.GREY[2])
                        screen.SetPixel(24 - pixel[0], 13 - pixel[1],
                                        Util.GREY[0], Util.GREY[1], Util.GREY[2])

                for j in range(32):
                    for i in range(32):
                        dist = np.abs(j - Util.WIN_POS[1]) + np.abs(i - Util.WIN_POS[0])
                        if (dist <= Util.TICK % 64 and Util.TICK < -64) or (dist > Util.TICK % 64 and Util.TICK >= -64):
                            screen.SetPixel(j, i, Util.WIN_COLOR[0], Util.WIN_COLOR[1], Util.WIN_COLOR[2])
                Util.TICK += 1
                if Util.TICK == 0:
                    Util.GAME_STATE = "TITLE"
                    for line in self.tilemap:
                        for tile in line:
                            tile.type = "EMPTY"
                self.timer.tick()
                screen = self.matrix.SwapOnVSync(screen)


# Main function
if __name__ == "__main__":
    snake = Snake()
    if not snake.process():
        snake.print_help()
