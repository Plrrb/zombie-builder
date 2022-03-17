from game.creatures.player import Player

from game.utils.input import BooleanInput
from game.scenes.editor import EditorScene
from game.utils.player_controller import PlayerController
from game.config import UP, DOWN, LEFT, RIGHT

# from game.scenes.survive import SurviveScene


class BackgroundScene:
    def __init__(self):
        self.player = Player()
        self.player_controller = PlayerController(self.player)
        self.editor = EditorScene()

        self.scene_update = self.update_editor
        self.inputs = BooleanInput()

    def draw(self):
        self.editor.draw()
        self.player.draw()

    def update(self, dt):
        self.scene_update(dt)
        self.player_controller.update(
            self.inputs[UP],
            self.inputs[DOWN],
            self.inputs[LEFT],
            self.inputs[RIGHT],
        )

    def update_editor(self, dt):
        self.editor.update(dt)
        self.player.update(dt)

    def on_key_press(self, symbol, modifiers):
        self.inputs.press(symbol)

    def on_key_release(self, symbol, modifiers):
        self.inputs.release(symbol)

    def on_mouse_motion(self, position):
        self.editor.on_mouse_motion(position)

    def on_mouse_press(self, position):
        self.editor.on_mouse_press(position)
