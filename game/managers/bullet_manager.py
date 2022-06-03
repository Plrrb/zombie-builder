from arcade import check_for_collision_with_list, SpriteList
from game.utils.bullet import Bullet


class BulletManager:
    def __init__(self):
        self.bullets = SpriteList()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

    def update(self, dt):
        self.bullets.update()

    def remove_bullets_outside(self, width, height):
        removed = []

        for bullet in self.bullets:
            if not (0 < bullet.position[0] < width and 0 < bullet.position[1] < height):
                removed.append(bullet)

        for bullet in removed:
            self.bullets.remove(bullet)

    def shoot_from(self, position, velocity):
        self.bullets.append(Bullet(position, velocity))

    def check_for_hits(self, sprite):
        return check_for_collision_with_list(sprite, self.bullets)

    def remove_all_in_list(self, hit_list):
        for hit in hit_list:
            self.bullets.remove(hit)
