from arcade import SpriteList, draw_xywh_rectangle_filled, load_texture
from arcade.key import MOD_SHIFT
from game.config import BLOCK_SIZE, WOOD_BLOCK_PATH
from game.utils.functions import fix_to_grid
from game.utils.vector import Vector2
from game.utils.block import WoodBlock


class EditorScene:
    def __init__(self):
        self.shadow = Vector2(0, 0)
        self.blocks = {}
        self.block_texture = load_texture(WOOD_BLOCK_PATH)

    def draw(self):

        for block in self.blocks:
            self.block_texture.draw_transformed(*block, *BLOCK_SIZE)
            # draw_xywh_rectangle_filled(*block, *BLOCK_SIZE, (255, 0, 0))

        draw_xywh_rectangle_filled(*self.shadow, *BLOCK_SIZE, (255, 255, 255))

    def update(self, dt):
        pass

    def place_block(self, position):
        position = fix_to_grid(position, BLOCK_SIZE)
        self.blocks[position] = None

    def on_mouse_motion(self, position):
        self.shadow = fix_to_grid(position, BLOCK_SIZE)

    def on_mouse_drag(self, position, modifiers):
        pos = fix_to_grid(position, BLOCK_SIZE)

        if not (modifiers & MOD_SHIFT):
            self.place_block(position)
        elif pos in self.blocks:
            del self.blocks[pos]

    def on_mouse_press(self, position, modifiers):
        pass

    def on_mouse_release(self, position, modifiers):
        pos = fix_to_grid(position, BLOCK_SIZE)

        if not (modifiers & MOD_SHIFT):
            self.place_block(position)
        elif pos in self.blocks:
            del self.blocks[pos]

    def get_blocks(self):
        bs = SpriteList(spatial_hash_cell_size=BLOCK_SIZE)

        for pos in self.blocks:
            bs.append(
                WoodBlock(
                    # i wish this drawed from the bottom left to top right like draw_xywh_rectangle_filled
                    center_x=pos.x + 25 / 2,
                    center_y=pos.y + 25 / 2,
                )
            )

        return bs
