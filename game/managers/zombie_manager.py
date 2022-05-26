import math

from arcade import check_for_collision_with_list, SpriteList
from game.config import HEIGHT, WIDTH
from game.creatures.zombie import Zombie


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
        self.zombies.append(Zombie([-100, HEIGHT / 2]))
        self.zombies.append(Zombie([WIDTH + 100, HEIGHT / 2]))
        self.zombies.append(Zombie([WIDTH / 2, HEIGHT + 100]))

    def send_attack(self, thing):
        for zombie in self.zombies:
            zombie.attack(thing)
