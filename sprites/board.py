from constants import *
from sprites.fruit import Fruit
from sprites.snake import Snake


class Board:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake(self.fruit)
        self.increased = False
        self.score = 0

        self.timer = 0

    def draw(self, window):
        self.fruit.draw(window)
        self.snake.draw(window)

    def move(self):
        self.timer += 1

        if self.timer > (400 * ((self.score**2 + 1) / (self.score + 1))):
            self.snake.is_dead = True
        # Check for eaten and reposition
        if self.snake.eaten:
            self.score += 1
            self.increased = True
            self.timer = 0
            while True:
                new_position = self.fruit.set_up_position()

                inside = False
                for block in self.snake.body:
                    if new_position == block:
                        inside = True
                        break
                if not inside:
                    self.snake.eaten = False
                    break

        self.snake.move_if_able()

    def get_input(self):
        input = []

        input.append(self.snake.body[0][0] - self.fruit.position[0])
        input.append(self.snake.body[0][1] - self.fruit.position[1])

        top_left = (
            self.snake.body[0][0] - 2,
            self.snake.body[0][1] - 2,
        )

        input.append(self.snake.length)

        for y in range(5):
            for x in range(5):

                loc = (
                    top_left[0] + x,
                    top_left[1] + y
                )
                if self.fruit.position == loc:
                    input.append(2)
                elif loc[0] > BOARD_WIDTH-1 or loc[0] < 0 or loc[1] > BOARD_HEIGHT-1 or loc[1] < 0:
                    input.append(3)
                elif self.snake.contains(loc):
                    input.append(1)
                else:
                    input.append(0)

        # print(input)
        return input
