from game.config import BULLET_TO_ZOMBIE_DAMAGE, HEIGHT, WIDTH, ZOMBIE_TO_BLOCK_DAMAGE
from game.managers.bullet_manager import BulletManager
from game.managers.zombie_manager import ZombieManager


class SurviveScene:
    def __init__(self, blocks):
        self.blocks = blocks
        self.bullet_manager = BulletManager()
        self.zombie_manager = ZombieManager()
        self.zombie_manager.spawn_zombies(3)

    def deal_bullet_damage_to_zombies(self, dt):
        for zombie in self.zombie_manager.zombies:
            damage = (
                len(self.bullet_manager.check_for_hits(zombie))
                * BULLET_TO_ZOMBIE_DAMAGE
                * dt
            )

            if zombie.sub_health(damage):
                self.zombie_manager.remove_zombie(zombie)

    def deal_damage_to_blocks_by_zombies(self, dt):
        for block in self.blocks:
            if self.zombie_manager.check_for_hits(block) and block.sub_health(
                ZOMBIE_TO_BLOCK_DAMAGE * dt
            ):

                # blocks_to_be_removed = set(blocks_to_be_removed)
                self.blocks.remove(block)

    def update(self, dt):
        self.zombie_manager.update(dt)
        self.bullet_manager.update(dt)
        self.bullet_manager.remove_bullets_outside(WIDTH, HEIGHT)

        self.deal_bullet_damage_to_zombies(dt)
        self.deal_damage_to_blocks_by_zombies(dt)

    def send_attack(self, player):
        self.zombie_manager.send_attack(player)

    def draw(self):
        self.blocks.draw()
        self.bullet_manager.draw()
        self.zombie_manager.draw()

    def shoot(self, position, velocity):
        self.bullet_manager.shoot_at(position, velocity)

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
