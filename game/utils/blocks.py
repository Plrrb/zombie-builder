from arcade import Sprite
from game.config import (
    METAL_BLOCK_HEALTH,
    WOOD_BLOCK_HEALTH,
    WOOD_BLOCK_PATH,
    METAL_BLOCK_PATH,
    BLOCK_SIZE,
)
from game.managers.health_manager import HealthManager


class Block(Sprite):
    def __init__(self, image, pos, health):
        super().__init__(
            image,
            center_x=pos[0] + BLOCK_SIZE[0] / 2,
            center_y=pos[1] + BLOCK_SIZE[1] / 2,
        )
        self.max_health = health
        self.health = HealthManager(health)

    def sub_health(self, value):
        if self.health.sub_health(value):
            self.alpha = 0
            return True
        else:
            self.alpha = (255 / self.max_health) * self.health.health
            return False


class WoodBlock(Block):
    def __init__(self, pos):
        super().__init__(WOOD_BLOCK_PATH, pos, WOOD_BLOCK_HEALTH)


class MetalBlock(Block):
    def __init__(self, pos):
        super().__init__(METAL_BLOCK_PATH, pos, METAL_BLOCK_HEALTH)
