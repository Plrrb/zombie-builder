from arcade import Sprite

# from game.utils.vector import Vector2


class Player(Sprite):
    def __init__(self):
        super().__init__(":resources:images/animated_characters/robot/robot_idle.png")
        self.position = [200, 200]
        self.velocity = [0, 0]
        # self.size = Vector2(50, 50)
        # self.color = (255, 0, 127)
        self.max_speed = (5, 5)
        self.friction = (0.5, 0.5)

    def update(self, dt):
        super().update()
        # self.update_position(dt)

    # def update_position(self, dt):
    #     self.position += self.velocity * (dt, dt)

    def move(self, x, y):
        self.velocity = [x * self.max_speed[0], y * self.max_speed[1]]
