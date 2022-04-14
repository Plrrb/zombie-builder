from game.config import DOWN, LEFT, RIGHT, UP
from game.creatures.player import Player
from game.scenes.editor import EditorScene
from game.scenes.survive import SurviveScene
from game.utils.button import Button
from game.utils.input import BooleanInput
from game.utils.player_controller import PlayerController
from game.utils.vector import Vector2
from arcade import PhysicsEngineSimple

from game.utils.functions import combine_lists


class BackgroundScene:
    def __init__(self):
        self.player = Player()
        self.inputs = BooleanInput()
        self.player_controller = PlayerController(self.player)
        self.editor = EditorScene()

        self.scene = self.editor
        self.scene_update = self.update_editor
        self.scene_draw = self.editor.draw

        self.play_button = Button(
            Vector2(100, 100), Vector2(100, 100), self.switch_to_survive_scene
        )

    def draw(self):
        self.scene_draw()
        self.player.draw()
        self.play_button.draw()

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
        self.survive_scene.update(dt)
        self.survive_scene.send_attack(self.player)

        for engine in self.physics_engines:
            engine.update()

    def switch_to_survive_scene(self):
        self.blocks = self.editor.get_blocks()
        self.survive_scene = SurviveScene(self.blocks)
        self.zombies = self.survive_scene.zombies

        self.scene_update = self.update_survive
        self.scene_draw = self.survive_scene.draw

        self.physics_engines = []

        self.physics_engines.append(
            PhysicsEngineSimple(self.player, combine_lists(self.blocks, self.zombies))
        )

        for zombie in self.zombies:
            self.physics_engines.append(PhysicsEngineSimple(zombie, self.blocks))

    def on_key_press(self, symbol, modifiers):
        self.inputs.press(symbol)

    def on_key_release(self, symbol, modifiers):
        self.inputs.release(symbol)

    def on_mouse_motion(self, position):
        self.scene.on_mouse_motion(position)

    def on_mouse_press(self, position, modifiers):
        self.play_button.update(position)
        self.scene.on_mouse_press(position, modifiers)

    def on_mouse_drag(self, position, modifiers):
        self.scene.on_mouse_drag(position, modifiers)

    def on_mouse_release(self, position, modifiers):
        self.scene.on_mouse_release(position, modifiers)
