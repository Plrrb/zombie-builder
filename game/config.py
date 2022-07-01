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

SELECT_WOOD_BLOCK = key.KEY_1
SELECT_METAL_BLOCK = key.KEY_2

# Image Paths
WOOD_BLOCK_PATH = "game/images/wood_block.png"
METAL_BLOCK_PATH = "game/images/metal_block.png"

BULLET_PATH = ":resources:images/space_shooter/laserBlue01.png"
ZOMBIE_PATH = ":resources:images/animated_characters/zombie/zombie_idle.png"
PLAYER_PATH = ":resources:images/animated_characters/robot/robot_idle.png"

# Health Values
PLAYER_HEALTH = 100
WOOD_BLOCK_HEALTH = 100
METAL_BLOCK_HEALTH = 360

# Damage Settings (they will be multiplied by delta time so they are acually smaller)
BULLET_TO_ZOMBIE_DAMAGE = 15
ZOMBIE_TO_PLAYER_DAMAGE = 20
BULLET_TO_BLOCK_DAMAGE = 200

# Speeds
BULLET_SPEED = (5, 5)
PLAYER_SPEED = (6, 6)

FIRE_RATE = 0.5

# Sizes
BLOCK_SIZE = (25, 25)

# Sounds
SHOOT_SOUND = ":resources:sounds/fall3.wav"

ZOMBIES = {
    "default": {
        "speed": (2, 2),
        "max_health": 100,
        "damage": 20,
        "block_damage": 30,
        "image": ":resources:images/animated_characters/zombie/zombie_idle.png",
    },
    "fast": {
        "speed": (8, 8),
        "max_health": 75,
        "image": "game/images/flash.png",
    },
    "slow": {},
}
