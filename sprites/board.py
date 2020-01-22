from sprites.fruit import Fruit
from sprites.snake import Snake


class Board:
    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake(self.fruit)
        self.score = 0

    def draw(self, window):
        # Check for eaten and reposition
        if self.snake.eaten:
            self.score += 1
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
        self.fruit.draw(window)
        self.snake.draw(window)
