import pygame
import neat

from sprites.board import Board
from sprites.fruit import Fruit
from sprites.snake import Snake

pygame.font.init()
from constants import *


def draw_window(window, board: Board):
    window.fill((0, 0, 0))
    board.draw(window)
    pygame.display.update()


GEN = 0


def main():
    global GEN

    board = Board()

    window = pygame.display.set_mode((BLOCK_SIZE * BOARD_WIDTH, BLOCK_SIZE * BOARD_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    board.snake.face(LEFT)
                if event.key == pygame.K_d:
                    board.snake.face(RIGHT)
                if event.key == pygame.K_w:
                    board.snake.face(UP)
                if event.key == pygame.K_s:
                    board.snake.face(DOWN)

        if board.snake.is_dead:
            run = False
            pygame.quit()
            quit()

        draw_window(window, board)


if __name__ == '__main__':
    main()
