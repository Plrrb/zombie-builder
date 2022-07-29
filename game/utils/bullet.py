import math

from arcade import Sprite
from game.config import BULLET_SPEED


class Bullet(Sprite):
    def __init__(self, image_path, position, velocity):
        super().__init__(image_path)
        self.position = position
        self.velocity = (velocity[0] * BULLET_SPEED[0], velocity[1] * BULLET_SPEED[1])
        self.rotate_towards(velocity)

    def rotate_towards(self, velocity):
        angle = math.atan2(velocity[1], velocity[0])
        angle_deg = math.degrees(angle)

        if angle_deg < 0:
            angle_deg += 360

        self.angle = angle_deg

    def curve(self, position):
        # x = position[0] - self.position[0]
        # y = position[1] - self.position[1]

        # self.velocity = (x / 50, y / 50)

        target_angle = math.atan2(
            self.position[1] - position[1], self.position[0] - position[0]
        )

        if self.angle > target_angle:
            self.angle -= 0.1
            self.rotate_velocity(0.01)

        elif self.angle < target_angle:
            self.angle += 0.1
            self.rotate_velocity(-0.01)

    def rotate_velocity(self, angle):
        x = self.velocity[0] * math.cos(angle) - self.velocity[1] * math.sin(angle)
        y = self.velocity[0] * math.sin(angle) + self.velocity[1] * math.cos(angle)

        self.velocity = (x, y)
