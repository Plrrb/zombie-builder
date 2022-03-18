from arcade import draw_xywh_rectangle_filled
from arcade.key import MOD_SHIFT
from game.utils.functions import fix_to_grid
from game.utils.vector import Vector2


class EditorScene:
    def __init__(self):
        self.shadow = Vector2(0, 0)
        self.blocks = {}
        self.block_size = Vector2(25, 25)

    def draw(self):
        draw_xywh_rectangle_filled(*self.shadow, *self.block_size, (255, 255, 255))

        for block in self.blocks:
            draw_xywh_rectangle_filled(*block, *self.block_size, (255, 0, 0))

    def update(self, dt):
        pass

    def place_block(self, position):
        position = fix_to_grid(position, self.block_size)
        self.blocks[tuple(position)] = None

    def on_mouse_motion(self, position):
        self.shadow = fix_to_grid(position, self.block_size)

    def on_mouse_drag(self, position, modifiers):
        pos = tuple(fix_to_grid(position, self.block_size))

        if not (modifiers & MOD_SHIFT):
            self.place_block(position)
        elif pos in self.blocks:
            del self.blocks[pos]

    def on_mouse_press(self, position, modifiers):
        pass

    def on_mouse_release(self, position, modifiers):
        pos = tuple(fix_to_grid(position, self.block_size))

        if not (modifiers & MOD_SHIFT):
            self.place_block(position)
        elif pos in self.blocks:
            del self.blocks[pos]
