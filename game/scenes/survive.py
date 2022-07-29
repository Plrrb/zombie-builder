from arcade import SpriteList, check_for_collision_with_list
from game.managers.zombie_manager import ZombieManager


class SurviveScene:
    def __init__(self, blocks: SpriteList):
        self.blocks = blocks
        self.zombie_manager = ZombieManager()

        self.wave_level = 5
        self.zombie_manager.spawn_zombies(self.wave_level)

    def draw(self):
        self.blocks.draw()
        self.zombie_manager.draw()

    def update(self, dt):
        self.zombie_manager.update(dt)

        self.deal_damage_to_blocks_by_zombies(dt)

        if len(self.zombie_manager.zombies) == 0:
            self.wave_level += 1
            self.zombie_manager.spawn_zombies(self.wave_level)

    def deal_damage_to_blocks_by_zombies(self, dt):
        for block in self.blocks:

            damage = sum(
                zombie.block_damage
                for zombie in self.zombie_manager.get_zombies_that_hit(block)
            )

            if block.sub_health(damage * dt):
                self.blocks.remove(block)

    def sprite_collides_with_block(self, sprite, damage):
        hits = check_for_collision_with_list(sprite, self.blocks)

        for hit in hits:
            if hit.sub_health(damage):
                self.blocks.remove(hit)

        return hits

    def do_damage_to_all_colliding_zombies(self, sprites, damage):
        self.zombie_manager.do_damage_to_all_colliding_zombies(sprites, damage)

    def get_zombies_that_hit(self, sprite):
        return self.zombie_manager.get_zombies_that_hit(sprite)

    def get_zombie_damage_to(self, sprite):
        return self.zombie_manager.get_zombie_damage_to(sprite)

    def send_attack(self, sprite):
        self.zombie_manager.send_attack(sprite.position)

    def get_zombies(self):
        return self.zombie_manager.zombies

    def on_mouse_press(self, position, modifiers):
        pass

    def on_mouse_release(self, position, modifiers):
        pass

    def on_mouse_motion(self, position):
        pass

    def on_mouse_drag(self, position, modifiers):
        pass
