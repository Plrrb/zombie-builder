from arcade import check_for_collision_with_list, SpriteList, load_sound, play_sound
from game.utils.bullet import Bullet
from game.config import SHOOT_SOUND


class BulletManager:
    shoot_sound = load_sound(SHOOT_SOUND)

    def __init__(self, shoot_interval):
        self.shoot_interval = shoot_interval
        self.bullets = SpriteList()
        self.time_left_to_shoot = 0

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

    def update(self, dt):
        self.bullets.update()
        self.time_left_to_shoot -= dt

    def remove_bullets_outside(self, width, height):
        removed = []

        for bullet in self.bullets:
            if not (0 < bullet.position[0] < width and 0 < bullet.position[1] < height):
                removed.append(bullet)

        for bullet in removed:
            self.bullets.remove(bullet)

    def shoot_from(self, position, velocity):
        if self.time_left_to_shoot <= 0:
            self.bullets.append(Bullet(position, velocity))
            self.time_left_to_shoot = self.shoot_interval
            play_sound(self.shoot_sound, 1)

    def check_for_hits(self, sprite):
        return check_for_collision_with_list(sprite, self.bullets)

    def remove_all_in_list(self, hit_list):
        for hit in hit_list:
            self.bullets.remove(hit)
