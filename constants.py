import os

import pygame

BLOCK_SIZE = 34

BOARD_HEIGHT = 20
BOARD_WIDTH = 40

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

BLOCKS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('assets', 'GreenBlock.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('assets', 'RedBlock.png'))),
]

