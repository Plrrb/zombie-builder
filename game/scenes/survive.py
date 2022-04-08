from game.creatures.zombie import Zombie
import arcade


class SurviveScene:
    def __init__(self, blocks):
        self.blocks = blocks
        self.zombies = arcade.SpriteList()

        for i in range(3):
            self.zombies.append(Zombie([200 * i + 200, 200]))

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
