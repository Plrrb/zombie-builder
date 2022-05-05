from arcade import draw_xywh_rectangle_filled
from arcade.color import RED, GREEN


class HealthManager:
    def sub_health(self, value):
        self.health -= value
        return self.health <= 0

    def draw_health(self):
        x = self.position[0] - 50
        y = self.position[1] + 50
        draw_xywh_rectangle_filled(x, y, 100, 16, RED)
        draw_xywh_rectangle_filled(x, y, self.health, 16, GREEN)
