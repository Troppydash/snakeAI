from constants import *
from sprites.fruit import Fruit


class Snake:
    def __init__(self, fruit: Fruit, length=4):
        # Length and Body
        self.length = length
        self.body = []

        x = BOARD_WIDTH / 2
        y = BOARD_HEIGHT / 2
        for i in range(length):
            self.body.append(
                (x + i, y)
            )

        # Texture
        self.sprite = BLOCKS[0]

        # Movement
        self.facing = LEFT
        self.tick = 0

        # Eating Fruit
        self.fruit = fruit
        self.eaten = False
        self.ghost_block = ()

        self.is_dead = False

    def check_dead(self):
        for index, body in enumerate(self.body):
            # Out of bounds
            if body[0] > BOARD_WIDTH or body[0] < 0:
                return True
            elif body[1] > BOARD_HEIGHT or body[1] < 0:
                return True

            # Same Location
            for i, rep in enumerate(self.body):
                if body == rep and index != i:
                    return True
        return False

    def draw(self, window):
        self.tick += 1
        if self.tick > 7:
            self.move()
            self.tick = 0
            self.is_dead = self.check_dead()

        for block in self.body:
            window.blit(
                self.sprite,
                (
                    block[0] * BLOCK_SIZE,
                    block[1] * BLOCK_SIZE
                )
            )

    def face(self, new_direction):
        if self.facing % 2 == new_direction % 2:
            return
        self.facing = new_direction

    def move(self):
        new_body = []
        self.ghost_block = self.body[-1]

        for index, block in enumerate(self.body):
            if index == 0:
                if self.facing == LEFT:
                    new_body.append((
                        block[0] - 1,
                        block[1]
                    ))
                elif self.facing == RIGHT:
                    new_body.append((
                        block[0] + 1,
                        block[1]
                    ))
                elif self.facing == UP:
                    new_body.append((
                        block[0],
                        block[1] - 1
                    ))
                elif self.facing == DOWN:
                    new_body.append((
                        block[0],
                        block[1] + 1
                    ))

                # Check If Eaten Fruit
                if new_body[0] == self.fruit.position:
                    self.eaten = True
                    self.length += 1
                    self.body.append(self.ghost_block)

            else:
                new_body.append(self.body[index - 1])

        self.body = new_body
