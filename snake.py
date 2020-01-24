import pygame
import neat

from sprites.board import Board
from sprites.fruit import Fruit
from sprites.snake import Snake

pygame.font.init()
from constants import *


def draw_window(window, boards):
    window.fill((0, 0, 0))
    # for board in boards:
    #     board.draw(window)
    boards[0].draw(window)
    # print(boards[0].get_input())
    pygame.display.update()


GEN = 0
DED = 0

def main(genomes, config):
    global GEN
    global DED
    GEN += 1

    nets = []
    ge = []

    boards = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)

        boards.append(Board())



    window = pygame.display.set_mode((BLOCK_SIZE * BOARD_WIDTH, BLOCK_SIZE * BOARD_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_a:
            #         board.snake.face(LEFT)
            #     if event.key == pygame.K_d:
            #         board.snake.face(RIGHT)
            #     if event.key == pygame.K_w:
            #         board.snake.face(UP)
            #     if event.key == pygame.K_s:
            #         board.snake.face(DOWN)

        for index, board in enumerate(boards):
            board.move()

            input = board.get_input()
            output = nets[index].activate(
                input
            )

            up = output[0]
            down = output[1]
            left = output[2]
            right = output[3]

            var = {
                up: UP,
                down: DOWN,
                left: LEFT,
                right: RIGHT
            }
            board.snake.face(var.get(max(var)))

            if board.increased:
                ge[index].fitness += 10
                board.increased = False
            ge[index].fitness -= 0.001
            if board.snake.is_dead:
                ge[index].fitness -= 10
                boards.pop(index)
                ge.pop(index)
                nets.pop(index)
                DED += 1

        if len(boards) <= 0:
            run = False
            break

        draw_window(window, boards)


def run(config_path):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    population = neat.Population(config)

    population.add_reporter(neat.StdOutReporter(True))
    population.add_reporter(neat.StatisticsReporter())

    winner = population.run(main, 5000)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.feedforward.txt")
    run(config_path)
