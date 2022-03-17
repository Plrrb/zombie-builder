from arcade import draw_xywh_rectangle_filled
from game.utils.vector import Vector2


class Player:
    def __init__(self):
        self.position = Vector2(200, 200)
        self.velocity = Vector2(0, 0)
        self.size = Vector2(50, 50)
        self.color = (255, 0, 127)
        self.max_speed = Vector2(100, 100)
        self.friction = Vector2(0.5, 0.5)

    def draw(self):
        draw_xywh_rectangle_filled(*self.position, *self.size, self.color)

    def update(self, dt):
        self.update_position(dt)

    def update_position(self, dt):
        self.position += self.velocity * Vector2(dt, dt)

    def move(self, x, y):
        self.velocity = Vector2(x, y) * self.max_speed
