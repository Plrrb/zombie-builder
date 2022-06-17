from game.config import (
    BULLET_TO_BLOCK_DAMAGE,
    BULLET_TO_ZOMBIE_DAMAGE,
    HEIGHT,
    WIDTH,
    ZOMBIE_TO_BLOCK_DAMAGE,
)
from game.managers.bullet_manager import BulletManager
from game.managers.zombie_manager import ZombieManager


class SurviveScene:
    def __init__(self, blocks):
        self.blocks = blocks
        self.bullet_manager = BulletManager(1)
        self.zombie_manager = ZombieManager()
        self.zombie_manager.spawn_zombies(3)

    def deal_damage_to_blocks_by_zombies(self, dt):
        for block in self.blocks:
            if self.zombie_manager.check_for_hits(block) and block.sub_health(
                ZOMBIE_TO_BLOCK_DAMAGE * dt
            ):

                # blocks_to_be_removed = set(blocks_to_be_removed)
                self.blocks.remove(block)

    def do_bullet_to_blocks_collsion(self, dt):
        hits = []

        for block in self.blocks:
            hit = self.bullet_manager.check_for_hits(block)
            hits += hit
            damage = len(hit) * BULLET_TO_BLOCK_DAMAGE * dt

            if block.sub_health(damage):
                self.blocks.remove(block)

        hits = set(hits)

        self.bullet_manager.remove_all_in_list(hits)

    def update(self, dt):
        self.zombie_manager.update(dt)
        self.bullet_manager.remove_bullets_outside(WIDTH, HEIGHT)
        self.bullet_manager.update(dt)

        self.do_bullet_to_blocks_collsion(dt)

        self.zombie_manager.do_damage_to_all_colliding_zombies(
            self.bullet_manager.bullets, BULLET_TO_ZOMBIE_DAMAGE * dt
        )
        self.deal_damage_to_blocks_by_zombies(dt)

    def send_attack(self, player):
        self.zombie_manager.send_attack(player.position)

    def draw(self):
        self.blocks.draw()
        self.bullet_manager.draw()
        self.zombie_manager.draw()

    def shoot_from(self, position, velocity):
        self.bullet_manager.shoot_from(position, velocity)

    def get_sprite_to_zombie_hits(self, sprite):
        return self.zombie_manager.check_for_hits(sprite)

    def get_zombies(self):
        return self.zombie_manager.zombies

    def on_mouse_motion(self, position):
        pass

    def on_mouse_press(self, position, modifiers):
        pass

    def on_mouse_drag(self, position, modifiers):
        pass

    def on_mouse_release(self, position, modifiers):
        pass
