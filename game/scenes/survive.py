from game.creatures.player import Player
from game.creatures.zombie import Zombie


class SurviveScene:
    def __init__(self):
        self.player = Player()

    def update(self):
        self.player.update()
