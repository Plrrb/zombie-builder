from turtle import pos
from arcade import (
    PhysicsEngineSimple,
    check_for_collision_with_list,
    check_for_collision_with_lists,
)
from game.config import DOWN, HEIGHT, LEFT, RIGHT, UP, WIDTH, ZOMBIE_TO_PLAYER_DAMAGE
from game.creatures.player import Player
from game.scenes.editor import EditorScene
from game.scenes.survive import SurviveScene
from game.utils.button import Button
from game.utils.functions import combined_lists
from game.utils.input import BooleanInput
from game.utils.player_controller import PlayerController
from game.utils.vector import Vector2
from arcade import SpriteList
from game.config import BULLET_TO_ZOMBIE_DAMAGE
from game.utils.bullet import Bullet


class BackgroundScene:
    def __init__(self):
        self.player = Player()
        self.inputs = BooleanInput()
        self.player_controller = PlayerController(self.player)
        self.editor = EditorScene()

        self.scene = self.editor
        self.scene_update = self.update_editor
        self.scene_draw = self.editor.draw
        self.on_mouse_press = self.editor_on_mouse_press
        self.bullets = SpriteList()

        self.play_button = Button(
            Vector2(100, 100), Vector2(100, 100), self.switch_to_survive_scene
        )

    def draw(self):
        self.scene_draw()
        self.play_button.draw()
        self.player.draw()

        self.bullets.draw()

    def update(self, dt):
        self.scene_update(dt)

        self.player.update(dt)

        self.player_controller.update(
            self.inputs[UP],
            self.inputs[DOWN],
            self.inputs[LEFT],
            self.inputs[RIGHT],
        )

    def update_editor(self, dt):
        self.editor.update(dt)

    def update_survive(self, dt):
        self.bullets.update()
        for bullet in self.bullets:
            if not Vector2(*bullet.position).inbounds((0, 0), (WIDTH, HEIGHT)):
                self.bullets.remove(bullet)
                print("bullet removed")

        for engine in self.physics_engines:
            engine.update()

        self.survive_scene.update(dt)
        self.survive_scene.send_attack(self.player)

        zombies_to_be_removed = []

        for zombie in self.survive_scene.zombies:
            if zombie.sub_health(
                len(check_for_collision_with_list(zombie, self.bullets))
                * BULLET_TO_ZOMBIE_DAMAGE
                * dt
            ):
                zombies_to_be_removed.append(zombie)

        for zombie in zombies_to_be_removed:
            self.survive_scene.zombies.remove(zombie)

        hits = len(
            check_for_collision_with_list(self.player, self.survive_scene.zombies)
        )

        self.player.sub_health(hits * ZOMBIE_TO_PLAYER_DAMAGE * dt)

    def switch_to_survive_scene(self):
        self.survive_scene = SurviveScene(self.editor.get_blocks())
        self.zombies = self.survive_scene.zombies

        self.scene_update = self.update_survive
        self.scene_draw = self.survive_scene.draw
        self.on_mouse_press = self.survive_on_mouse_press

        self.physics_engines = []

        blocks_and_zombies = SpriteList()

        for thing in combined_lists(self.survive_scene.blocks, self.zombies):
            blocks_and_zombies.append(thing)

        self.physics_engines.append(
            PhysicsEngineSimple(
                self.player,
                blocks_and_zombies,
            )
        )

        for zombie in self.zombies:
            self.physics_engines.append(
                PhysicsEngineSimple(zombie, self.survive_scene.blocks)
            )

    def on_key_press(self, symbol, modifiers):
        self.inputs.press(symbol)

    def on_key_release(self, symbol, modifiers):
        self.inputs.release(symbol)

    def on_mouse_motion(self, position):
        self.scene.on_mouse_motion(position)

    def editor_on_mouse_press(self, position, modifiers):
        self.play_button.update(position)
        self.scene.on_mouse_press(position, modifiers)

    def survive_on_mouse_press(self, position, modifiers):
        velocity = Vector2(*(position - Vector2(*self.player.position))).normalize()

        self.bullets.append(Bullet(self.player.position, velocity))
        self.scene.on_mouse_press(position, modifiers)

    def on_mouse_drag(self, position, modifiers):
        self.scene.on_mouse_drag(position, modifiers)

    def on_mouse_release(self, position, modifiers):
        self.scene.on_mouse_release(position, modifiers)
