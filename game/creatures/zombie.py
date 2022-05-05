from random import randint, random
import arcade
from game.config import ZOMBIE_PATH
from game.utils.vector import Vector2
from game.utils.health import HealthManager


class Zombie(arcade.Sprite, HealthManager):
    def __init__(self, position, max_speed):
        super().__init__(ZOMBIE_PATH)
        self.position = position
        self.health = 100

        s = random()
        self.max_speed = Vector2(*max_speed) - (s, s)

    def draw(self):
        super().draw()
        self.draw_health()

    def goto(self, pos):
        x = (pos[0] - self.position[0]) + randint(-250, 250)
        y = (pos[1] - self.position[1]) + randint(-250, 250)

        try:
            d = Vector2(x, y).normalize()
        except ZeroDivisionError:
            return

        self.velocity = list(d * self.max_speed)

    def attack(self, block):
        v = Vector2(block.position[0], block.position[1])
        self.goto(v)
