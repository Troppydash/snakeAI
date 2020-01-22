import random

from constants import *


class Fruit:
    def __init__(self):
        self.sprite = BLOCKS[1]
        self.position = (0, 0)
        self.set_up_position()

    def set_up_position(self):
        self.position = (
            random.randrange(0, BOARD_WIDTH),
            random.randrange(0, BOARD_HEIGHT)
        )
        return self.position

    def draw(self, window):
        window.blit(
            self.sprite,
            (
                self.position[0] * BLOCK_SIZE,
                self.position[1] * BLOCK_SIZE
            )
        )