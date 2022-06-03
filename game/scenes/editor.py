from arcade import SpriteList, draw_xywh_rectangle_filled, load_texture
from arcade.key import MOD_SHIFT
from game.config import BLOCK_SIZE, METAL_BLOCK_PATH, WOOD_BLOCK_PATH
from game.utils.blocks import WoodBlock, MetalBlock
from game.utils.button import Button
from game.utils.functions import fix_to_grid
from game.utils.vector import Vector2
from game.config import WIDTH, HEIGHT


class EditorScene:
    def __init__(self):
        self.shadow = Vector2(0, 0)
        self.blocks = {}
        self.wood_block_texture = load_texture(WOOD_BLOCK_PATH)
        self.metal_block_texture = load_texture(METAL_BLOCK_PATH)

        self.play_button = Button(Vector2(100, 100), Vector2(100, 100))
        self.selected_block = self.wood_block_texture

    def draw(self):
        for block in self.blocks:
            self.blocks[block].draw_transformed(*block, *BLOCK_SIZE)

        draw_xywh_rectangle_filled(*self.shadow, *BLOCK_SIZE, (255, 255, 255))
        self.play_button.draw()

    def update(self, dt):
        pass

    def place_block(self, position):
        position = fix_to_grid(position, BLOCK_SIZE)
        self.blocks[position] = self.selected_block

    def set_block_type_wood(self):
        self.selected_block = self.wood_block_texture

    def set_block_type_metal(self):
        self.selected_block = self.metal_block_texture

    def on_mouse_motion(self, position):
        self.shadow = fix_to_grid(position, BLOCK_SIZE)

    def on_mouse_drag(self, position, modifiers):
        pos = fix_to_grid(position, BLOCK_SIZE)
        if position[0] > WIDTH - 50:
            return

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

    def make_block(self, pos):
        if self.blocks[pos] == self.wood_block_texture:
            return WoodBlock(pos)

        elif self.blocks[pos] == self.metal_block_texture:
            return MetalBlock(pos)

    def get_blocks(self):
        bs = SpriteList(spatial_hash_cell_size=BLOCK_SIZE)

        for pos in self.blocks:
            bs.append(self.make_block(pos))

        return bs
