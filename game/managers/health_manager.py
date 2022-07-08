from arcade import draw_xywh_rectangle_filled
from arcade.color import GREEN, RED


class HealthManager:
    def __init__(self, max_health):
        self.max_health = max_health
        self.health = max_health

    def sub_health(self, value):
        self.health -= value
        return self.health <= 0

    def draw_health_bar(self, x, y):
        x -= 50

        width = (100 / self.max_health) * self.health

        draw_xywh_rectangle_filled(x, y, 100, 16, RED)
        draw_xywh_rectangle_filled(x, y, width, 16, GREEN)
