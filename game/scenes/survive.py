from game.config import HEIGHT, WIDTH, ZOMBIE_SPEED
from game.creatures.zombie import Zombie
import arcade


class SurviveScene:
    def __init__(self, blocks):
        self.blocks = blocks
        self.zombies = arcade.SpriteList()
        self.spawn_zombies(1)

    def spawn_zombies(self, nzombies):
        self.zombies.append(Zombie([-100, HEIGHT / 2], ZOMBIE_SPEED))
        self.zombies.append(Zombie([WIDTH + 100, HEIGHT / 2], ZOMBIE_SPEED))
        self.zombies.append(Zombie([WIDTH / 2, HEIGHT + 100], ZOMBIE_SPEED))

    def update(self, dt):
        self.zombies.update()

    def send_attack(self, player):
        for zombie in self.zombies:
            zombie.attack(player)

    def draw(self):
        self.blocks.draw()
        self.zombies.draw()

    def on_mouse_motion(self, position):
        pass

    def on_mouse_press(self, position, modifiers):
        pass

    def on_mouse_drag(self, position, modifiers):
        pass

    def on_mouse_release(self, position, modifiers):
        pass
