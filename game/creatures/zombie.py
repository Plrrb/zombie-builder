from random import randint, random

import arcade
from game.config import ZOMBIE_HEALTH, ZOMBIE_PATH, ZOMBIE_SPEED
from game.managers.health_manager import HealthManager
from game.utils.vector import Vector2


class Zombie(arcade.Sprite):
    def __init__(self, position):
        super().__init__(ZOMBIE_PATH)
        self.position = position
        self.health = HealthManager(ZOMBIE_HEALTH)

        s = random()
        self.max_speed = Vector2(*ZOMBIE_SPEED) - (s, s)

    def sub_health(self, value):
        return self.health.sub_health(value)

    def draw(self):
        super().draw()
        self.health.draw_health_bar(*self.position)

    def goto(self, pos):
        x = pos[0] - self.position[0]
        y = pos[1] - self.position[1]

        try:
            d = Vector2(x, y).normalize()
        except ZeroDivisionError:
            return

        self.velocity = list(d * self.max_speed)

    def attack(self, position):
        v = Vector2(position[0], position[1])
        self.goto(v)
