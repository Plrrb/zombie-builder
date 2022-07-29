import arcade
from game.config import ZOMBIE_BULLET_PATH, ZOMBIES
from game.managers.bullet_manager import BulletManager
from game.managers.health_manager import HealthManager
from game.utils.vector import Vector2


class Zombie(arcade.Sprite):
    player_damage = 0
    block_damage = 0

    def __init__(self, position, image, max_health, speed, player_damage, block_damage):
        super().__init__(image)
        self.position = position
        self.health = HealthManager(max_health)
        self.max_speed = Vector2(*speed)
        self.player_damage = player_damage
        self.block_damage = block_damage

    def draw(self):
        super().draw()

    def sub_health(self, value):
        return self.health.sub_health(value)

    def goto(self, pos):
        x = pos[0] - self.position[0]
        y = pos[1] - self.position[1]

        d = Vector2(x, y).normalize()

        self.velocity = list(d * self.max_speed)

    def damage_to(self, sprite):
        if arcade.check_for_collision(self, sprite):
            return self.player_damage
        return 0


class DefaultZombie(Zombie):
    def __init__(self, position):
        super().__init__(position, **ZOMBIES["default"])

    def draw(self):
        super().draw()
        self.health.draw_health_bar(self.position[0], self.position[1] + 40)

    def attack(self, position):
        v = Vector2(position[0], position[1])
        self.goto(v)


class FastZombie(DefaultZombie, Zombie):
    def __init__(self, position):
        Zombie.__init__(self, position, **ZOMBIES["fast"])

    def draw(self):
        Zombie.draw(self)
        self.health.draw_health_bar(self.position[0], self.position[1] + 50)


class SlowZombie(Zombie):
    def __init__(self, position):
        super().__init__(position, **ZOMBIES["slow"])
        self.bullet_manager = BulletManager(ZOMBIE_BULLET_PATH, 2)

    def draw(self):
        super().draw()

        self.bullet_manager.draw()
        self.health.draw_health_bar(self.position[0], self.position[1] + 75)

    def update(self):
        super().update()

        self.bullet_manager.update(1 / 60)

    def attack(self, position):
        self.goto(position)
        self.bullet_manager.shoot_from_start_to_target(self.position, position)
        self.bullet_manager.curve_bullets(position)

    def damage_to(self, sprite):
        bullet_damage = (
            len(self.bullet_manager.check_for_hits(sprite)) * self.player_damage
        )

        if arcade.check_for_collision(self, sprite):
            return super().damage_to(sprite) + bullet_damage

        return bullet_damage
