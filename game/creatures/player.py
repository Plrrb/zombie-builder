from arcade import Sprite
from game.config import (
    FIRE_RATE,
    HEIGHT,
    PLAYER_HEALTH,
    PLAYER_PATH,
    PLAYER_SPEED,
    WIDTH,
)
from game.managers.health_manager import HealthManager
from game.managers.bullet_manager import BulletManager


class Player(Sprite):
    def __init__(self):
        super().__init__(PLAYER_PATH)
        self.position = [200, 200]
        self.velocity = [0, 0]
        self.friction = (0.5, 0.5)
        self.max_speed = PLAYER_SPEED
        self.health = HealthManager(PLAYER_HEALTH)
        self.bullet_manager = BulletManager(FIRE_RATE)

    def draw(self):
        super().draw()
        self.health.draw_health_bar(self.position[0], self.position[1] + 50)
        self.bullet_manager.draw()

    def update(self, dt):
        super().update()
        self.bullet_manager.update(dt)
        self.bullet_manager.remove_bullets_outside(WIDTH, HEIGHT)

    def sub_health(self, damage):
        return self.health.sub_health(damage)

    def shoot_at(self, position):
        self.bullet_manager.shoot_from_start_to_target(self.position, position)

    def move(self, x, y):
        self.velocity = [x * self.max_speed[0], y * self.max_speed[1]]

    def get_bullets(self):
        return self.bullet_manager.bullets

    def remove_bullet(self, bullet):
        self.bullet_manager.remove_bullet(bullet)
