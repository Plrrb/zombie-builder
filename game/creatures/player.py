from arcade import Sprite
from game.config import PLAYER_PATH, PLAYER_SPEED
from game.managers.health_manager import HealthManager


class Player(Sprite, HealthManager):
    def __init__(self):
        super().__init__(PLAYER_PATH)
        self.position = [200, 200]
        self.velocity = [0, 0]
        self.max_speed = PLAYER_SPEED
        self.friction = (0.5, 0.5)
        self.health = 100

    def draw(self):
        super().draw()
        self.draw_health_bar()

    def update(self, dt):
        super().update()

    def move(self, x, y):
        self.velocity = [x * self.max_speed[0], y * self.max_speed[1]]
