from arcade import PhysicsEngineSimple
from game.config import DOWN, LEFT, RIGHT, UP, ZOMBIE_TO_PLAYER_DAMAGE
from game.creatures.player import Player
from game.managers.player_controller import PlayerController
from game.scenes.editor import EditorScene
from game.scenes.survive import SurviveScene
from game.utils.input import BooleanInput
from game.utils.vector import Vector2


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

    def draw(self):
        self.scene_draw()
        self.player.draw()

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

        self.deal_zombie_to_player_damage(dt)

    def deal_zombie_to_player_damage(self, dt):
        hits = len(self.survive_scene.get_sprite_to_zombie_hits(self.player))
        if self.player.sub_health(hits * ZOMBIE_TO_PLAYER_DAMAGE * dt):
            print("you dead...")

    def switch_to_survive_scene(self):
        self.survive_scene = SurviveScene(self.editor.get_blocks())
        self.zombies = self.survive_scene.get_zombies()

        self.scene = self.survive_scene
        self.scene_update = self.update_survive
        self.scene_draw = self.survive_scene.draw
        self.on_mouse_press = self.survive_on_mouse_press

        self.physics_engines = []

        self.physics_engines.append(
            PhysicsEngineSimple(
                self.player,
                self.survive_scene.blocks,
            )
        )

        self.physics_engines.append(
            PhysicsEngineSimple(
                self.player,
                self.zombies,
            )
        )

        for zombie in self.zombies:
            self.physics_engines.append(
                PhysicsEngineSimple(zombie, self.survive_scene.blocks)
            )

    def editor_on_mouse_press(self, position, modifiers):
        self.scene.on_mouse_press(position, modifiers)

        if self.editor.play_button.is_pressed(position):
            self.switch_to_survive_scene()

    def survive_on_mouse_press(self, position, modifiers):
        self.scene.on_mouse_press(position, modifiers)
        velocity = (
            position[0] - self.player.position[0],
            position[1] - self.player.position[1],
        )

        velocity = Vector2(*velocity).normalize()

        self.survive_scene.shoot_from(self.player.position, velocity)

    def on_key_press(self, symbol, modifiers):
        self.inputs.press(symbol)

    def on_key_release(self, symbol, modifiers):
        self.inputs.release(symbol)

    def on_mouse_motion(self, position):
        self.scene.on_mouse_motion(position)

    def on_mouse_drag(self, position, modifiers):
        self.scene.on_mouse_drag(position, modifiers)

    def on_mouse_release(self, position, modifiers):
        self.scene.on_mouse_release(position, modifiers)
