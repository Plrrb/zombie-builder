from arcade import draw_xywh_rectangle_filled


class Button:
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def draw(self):
        draw_xywh_rectangle_filled(*self.position, *self.size, color=(255, 255, 255))

    def is_pressed(self, pos):
        return pos.inbounds(self.position, (self.position + self.size))
