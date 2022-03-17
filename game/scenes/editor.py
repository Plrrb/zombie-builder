from arcade import draw_xywh_rectangle_filled
from game.utils.functions import fix_to_grid
from game.utils.vector import Vector2


class EditorScene:
    def __init__(self):
        self.shadow_pos = Vector2(0, 0)
        self.blocks = []
        self.block_size = Vector2(25, 25)

    def draw(self):
        draw_xywh_rectangle_filled(*self.shadow_pos, *self.block_size, (255, 255, 255))

        for block in self.blocks:
            draw_xywh_rectangle_filled(*block, *self.block_size, (128, 128, 128))

    def place_block(self, position):
        # we need to check if the pos is alread filled
        self.blocks.append(fix_to_grid(position, self.block_size))

    def update(self, dt):
        pass

    def on_mouse_motion(self, position):
        self.shadow_pos = fix_to_grid(position, self.block_size)

    def on_mouse_press(self, position):
        self.place_block(position)
