from arcade import Sprite
from game.config import WOOD_BLOCK_PATH, METAL_BLOCK_PATH, BLOCK_SIZE
from game.managers.health_manager import HealthManager


class Block(Sprite, HealthManager):
    def __init__(self, image, pos):
        super().__init__(
            image,
            center_x=pos[0] + BLOCK_SIZE[0] / 2,
            center_y=pos[1] + BLOCK_SIZE[1] / 2,
        )
        self.max_health = 100
        self.health = 100

    def sub_health(self, value):
        if HealthManager.sub_health(self, value):
            self.alpha = 0
            return True
        else:
            self.alpha = (255 / self.max_health) * self.health
            return False


class WoodBlock(Block):
    def __init__(self, pos):
        super().__init__(WOOD_BLOCK_PATH, pos)


class MetalBlock(Block):
    def __init__(self, pos):
        super().__init__(METAL_BLOCK_PATH, pos)
        self.max_health = 360
        self.health = 360
