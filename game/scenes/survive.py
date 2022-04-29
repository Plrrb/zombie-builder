import math

import arcade
from game.config import HEIGHT, WIDTH, ZOMBIE_SPEED, ZOMBIE_TO_BLOCK_DAMAGE
from game.creatures.zombie import Zombie


class SurviveScene:
    def __init__(self, blocks):
        self.blocks = blocks
        self.zombies = arcade.SpriteList()
        # self.spawn_zombies(1)

    def spawn_zombies(self, nzombies):
        self.zombies.append(Zombie([-100, HEIGHT / 2], ZOMBIE_SPEED))
        self.zombies.append(Zombie([WIDTH + 100, HEIGHT / 2], ZOMBIE_SPEED))
        self.zombies.append(Zombie([WIDTH / 2, HEIGHT + 100], ZOMBIE_SPEED))

    def get_zombie_block_collision(self):
        hits = []

        for zombie in self.zombies:
            for block in self.blocks:
                # this collions sucks
                if math.dist(zombie.position, block.position) < 100:
                    hits.append(block)

        return hits

    def update(self, dt):
        self.zombies.update()
        hits = self.get_zombie_block_collision()
        self.zombie_hit_blocks(hits, ZOMBIE_TO_BLOCK_DAMAGE * dt)

    def zombie_hit_blocks(self, hit_blocks, damage):
        blocks_to_be_removed = []

        for block in hit_blocks:
            if block.sub_health(damage):
                blocks_to_be_removed.append(block)

        blocks_to_be_removed = set(blocks_to_be_removed)

        for block in blocks_to_be_removed:
            self.blocks.remove(block)

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
