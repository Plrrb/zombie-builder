import arcade
from game.managers.health_manager import HealthManager
from game.utils.vector import Vector2
from game.config import ZOMBIES


class Zombie(arcade.Sprite):
    def __init__(self, position, zombie_type):
        super().__init__(ZOMBIES[zombie_type]["image"])
        self.position = position
        self.health = HealthManager(ZOMBIES[zombie_type]["max_health"])
        self.max_speed = Vector2(*ZOMBIES[zombie_type]["speed"])

    def sub_health(self, value):
        return self.health.sub_health(value)

    def draw(self):
        super().draw()
        self.health.draw_health_bar(*self.position)


class DefaultZombie(Zombie):
    damage = ZOMBIES["default"]["damage"]
    block_damage = ZOMBIES["default"]["block_damage"]

    def __init__(self, position):
        super().__init__(position, "default")

    def goto(self, pos):
        x = pos[0] - self.position[0]
        y = pos[1] - self.position[1]

        d = Vector2(x, y).normalize()

        self.velocity = list(d * self.max_speed)

    def attack(self, position):
        v = Vector2(position[0], position[1])
        self.goto(v)


class FastZombie(DefaultZombie, Zombie):
    def __init__(self, position):
        Zombie.__init__(self, position, "fast")
