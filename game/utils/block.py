from arcade import Sprite
from game.config import WOOD_BLOCK_PATH


class WoodBlock(Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(WOOD_BLOCK_PATH, *args, **kwargs)
        self.health = 100

    def sub_health(self, value):
        self.health -= value

        if self.health <= 0:
            self.alpha = 0
            return True

        self.alpha = (255 / 100) * self.health

        return False
