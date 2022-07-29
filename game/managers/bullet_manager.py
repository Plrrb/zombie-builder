from arcade import SpriteList, check_for_collision_with_list, load_sound, play_sound
from game.config import SHOOT_SOUND
from game.utils.bullet import Bullet
from game.utils.vector import Vector2


class BulletManager:
    shoot_sound = load_sound(SHOOT_SOUND)

    def __init__(self, bullet_image_path, fire_rate):
        self.fire_rate = fire_rate
        self.bullets = SpriteList()
        self.time_left_to_shoot = 0
        self.bullet_image_path = bullet_image_path

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

    def shoot_from_start_to_target(self, start, target):
        if self.time_left_to_shoot > 0:
            return

        velocity = (
            target[0] - start[0],
            target[1] - start[1],
        )

        try:
            velocity = Vector2(*velocity).normalize()
        except ZeroDivisionError:
            velocity = (0, 0)

        self.bullets.append(Bullet(self.bullet_image_path, start, tuple(velocity)))
        self.time_left_to_shoot = self.fire_rate
        play_sound(self.shoot_sound, 1)

    def check_for_hits(self, sprite):
        return check_for_collision_with_list(sprite, self.bullets)

    def curve_bullets(self, position):
        for bullet in self.bullets:
            bullet.curve(position)

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def remove_all_bullets_in_list(self, bullets_to_be_removed):
        for hit in bullets_to_be_removed:
            self.bullets.remove(hit)
