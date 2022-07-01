import math

from arcade import check_for_collision_with_list, SpriteList
from game.config import HEIGHT, WIDTH
from game.creatures.zombie import DefaultZombie, FastZombie


class ZombieManager:
    def __init__(self) -> None:
        self.zombies = SpriteList()

    def draw(self):
        for zombie in self.zombies:
            zombie.draw()

    def remove_zombie(self, zombie):
        self.zombies.remove(zombie)

    def update(self, dt):
        self.zombies.update()

    def do_damage_to_all_colliding_zombies(self, sprite_list, damage):
        for zombie in self.zombies:
            z_damage = len(check_for_collision_with_list(zombie, sprite_list)) * damage

            if zombie.health.sub_health(z_damage):
                self.zombies.remove(zombie)

    def check_for_hits(self, sprite):
        hits = []

        for zombie in self.zombies:
            if math.dist(sprite.position, zombie.position) < 100:
                hits.append(zombie)

        return hits

        # return arcade.check_for_collision_with_list(sprite, self.zombies)

    def spawn_zombies(self, count):
        self.zombies.append(FastZombie([-100, HEIGHT / 2]))
        self.zombies.append(DefaultZombie([WIDTH + 100, HEIGHT / 2]))
        self.zombies.append(DefaultZombie([WIDTH / 2, HEIGHT + 100]))
        self.zombies.append(DefaultZombie([WIDTH / 2, -100]))

    def send_attack(self, position):
        left_side = [position[0] - 30, position[1]]
        right_side = [position[0] + 30, position[1]]
        top_side = [position[0], position[1] + 30]
        bottom_side = [position[0], position[1] - 30]

        for zombie, position in zip(
            self.zombies, (left_side, right_side, top_side, bottom_side)
        ):
            zombie.attack(position)
