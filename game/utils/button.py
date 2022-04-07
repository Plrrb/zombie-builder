from arcade import draw_xywh_rectangle_filled


class Button:
    def __init__(self, position, size, on_click: callable):
        self.position = position
        self.size = size
        self.on_click = on_click

    def draw(self):
        draw_xywh_rectangle_filled(*self.position, *self.size, color=(255, 255, 255))

    def update(self, pos):
        if pos.inbounds(self.position, (self.position + self.size)):
            self.on_click()
