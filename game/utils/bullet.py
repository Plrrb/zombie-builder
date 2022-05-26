import math

from arcade import Sprite
from game.config import BULLET_PATH, BULLET_SPEED


class Bullet(Sprite):
    def __init__(self, position, velocity):
        super().__init__(BULLET_PATH)
        self.position = position
        self.velocity = velocity * BULLET_SPEED

        angle = math.atan2(velocity[1], velocity[0])
        angle_deg = math.degrees(angle)

        if angle_deg < 0:
            angle_deg += 360

        self.angle = angle_deg
