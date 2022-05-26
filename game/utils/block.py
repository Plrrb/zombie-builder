from arcade import Sprite
from game.config import WOOD_BLOCK_PATH
from game.managers.health_manager import HealthManager


class WoodBlock(Sprite, HealthManager):
    def __init__(self, *args, **kwargs):
        super().__init__(WOOD_BLOCK_PATH, *args, **kwargs)
        self.health = 100

    def sub_health(self, value):
        if HealthManager.sub_health(self, value):
            self.alpha = 0
            return True
        else:
            self.alpha = (255 / 100) * self.health
            return False
