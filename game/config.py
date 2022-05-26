# Window Settings
WIDTH = 1600
HEIGHT = 1000
TITLE = "Zombie Builder"

# Controls
from arcade import key

UP = key.W
DOWN = key.S
LEFT = key.A
RIGHT = key.D

# Image Paths
WOOD_BLOCK_PATH = "game/images/wood_block.png"
METAL_BLOCK_PATH = "game/images/metal_block.png"

BULLET_PATH = ":resources:images/space_shooter/laserBlue01.png"
ZOMBIE_PATH = ":resources:images/animated_characters/zombie/zombie_idle.png"
PLAYER_PATH = ":resources:images/animated_characters/robot/robot_idle.png"

# Damage Settings
ZOMBIE_TO_BLOCK_DAMAGE = 30
BULLET_TO_ZOMBIE_DAMAGE = 15
ZOMBIE_TO_PLAYER_DAMAGE = 20

# Speeds
BULLET_SPEED = (5, 5)
ZOMBIE_SPEED = (3, 3)
PLAYER_SPEED = (5, 5)

# Sizes
BLOCK_SIZE = (25, 25)
