import math

from arcade import Sprite
from game.config import BULLET_PATH, BULLET_SPEED


class Bullet(Sprite):
    def __init__(self, position, velocity):
        super().__init__(BULLET_PATH)
        self.position = position
        self.velocity = velocity * BULLET_SPEED

        # top right quadrant
        if velocity.x > 0 and velocity.y > 0:
            angle = math.atan(abs(velocity.y / velocity.x)) * 57.2958

        # top left quadrant:
        if velocity.x < 0 and velocity.y > 0:
            angle = math.atan(abs(velocity.x / velocity.y)) * 57.2958 + 90

        # bottom left quadrant
        if velocity.x < 0 and velocity.y < 0:
            angle = math.atan(abs(velocity.y / velocity.x)) * 57.2958 + 180

        # bottom right quadrant:
        if velocity.x > 0 and velocity.y < 0:
            angle = math.atan(abs(velocity.x / velocity.y)) * 57.2958 + 270

        self.angle = angle
