import arcade

from game.config import HEIGHT, TITLE, WIDTH
from game.scenes.background import BackgroundScene
from game.utils.input import BooleanInput
from game.utils.vector import Vector2


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.background_scene = BackgroundScene()
        self.mouse = Vector2(0, 0)
        self.inputs = BooleanInput()

    def on_draw(self):
        self.clear()
        self.background_scene.draw()

    def on_update(self, dt):
        self.background_scene.update(dt)

    def on_key_press(self, symbol, modifiers):
        self.inputs.press(symbol)
        self.background_scene.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.inputs.release(symbol)
        self.background_scene.on_key_release(symbol, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse = Vector2(x, y)
        self.background_scene.on_mouse_motion(self.mouse)

    def on_mouse_press(self, x, y, button, modifiers):
        self.mouse = Vector2(x, y)
        self.background_scene.on_mouse_press(self.mouse)

    def on_mouse_release(self, x, y, button, modifiers):
        self.inputs.release(button)
