class PlayerController:
    def __init__(self, player):
        self.player = player

    def update(self, up, down, left, right):

        d = 1
        if (up or down) and (left or right):
            d = 0.5
            # 0.7071067811865475

        self.player.move((right - left) * d, (up - down) * d)
