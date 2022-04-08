from arcade import Sprite
from game.config import WOOD_BLOCK_PATH


class WoodBlock(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(WOOD_BLOCK_PATH, *args, **kwargs)
        self.health = 100
