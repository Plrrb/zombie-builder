import arcade
from game.config import ZOMBIE_PATH
from game.utils.vector import Vector2


class Zombie(arcade.Sprite):
    def __init__(self, position):
        super().__init__(ZOMBIE_PATH)
        self.position = position
        self.max_speed = (4, 4)

    def goto(self, pos):
        x = pos[0] - self.position[0]
        y = pos[1] - self.position[1]

        self.velocity = list(Vector2(x, y).normalize() * self.max_speed)

    def attack(self, block):
        self.goto(block.position)
