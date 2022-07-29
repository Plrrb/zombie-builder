from arcade import PhysicsEngineSimple
from game.config import (
    BULLET_TO_BLOCK_DAMAGE,
    BULLET_TO_ZOMBIE_DAMAGE,
    DOWN,
    LEFT,
    RIGHT,
    SELECT_METAL_BLOCK,
    SELECT_WOOD_BLOCK,
    UP,
)
from game.creatures.player import Player
from game.managers.player_controller import PlayerController
from game.scenes.editor import EditorScene
from game.scenes.survive import SurviveScene
from game.utils.input import BooleanInput


class BackgroundScene:
    def __init__(self):
        self.player = Player()
        self.inputs = BooleanInput()
        self.player_controller = PlayerController(self.player)
        self.editor_scene = EditorScene()

        self.scene = self.editor_scene

    def draw(self):
        self.scene.draw()
        self.player.draw()

    def update(self, dt):
        self.scene.update(dt)
        self.player.update(dt)

        self.player_controller.update(
            self.inputs[UP],
            self.inputs[DOWN],
            self.inputs[LEFT],
            self.inputs[RIGHT],
        )

        if self.scene == self.editor_scene:
            self.update_editor(dt)
        elif self.scene == self.survive_scene:
            self.update_survive(dt)

    def update_editor(self, dt):
        if self.inputs[SELECT_WOOD_BLOCK]:
            self.editor_scene.set_block_type_wood()
        elif self.inputs[SELECT_METAL_BLOCK]:
            self.editor_scene.set_block_type_metal()

    def update_survive(self, dt):
        self.survive_scene.send_attack(self.player)

        for engine in self.physics_engines:
            engine.update()

        self.survive_scene.do_damage_to_all_colliding_zombies(
            self.player.get_bullets(), BULLET_TO_ZOMBIE_DAMAGE * dt
        )

        for bullet in self.player.get_bullets():
            if self.survive_scene.sprite_collides_with_block(
                bullet, BULLET_TO_BLOCK_DAMAGE * dt
            ):

                self.player.remove_bullet(bullet)

        # zombie_to_player_damage = sum(
        #     zombie.player_damage
        #     for zombie in self.survive_scene.get_zombies_that_hit(self.player)
        # )

        zombie_to_player_damage = self.survive_scene.get_zombie_damage_to(self.player)

        if self.player.sub_health(zombie_to_player_damage * dt):
            print("you dead")

    def switch_to_survive_scene(self):
        self.survive_scene = SurviveScene(self.editor_scene.get_blocks())
        self.zombies = self.survive_scene.get_zombies()

        self.scene = self.survive_scene

        self.physics_engines = [
            PhysicsEngineSimple(self.player, self.survive_scene.blocks)
        ]

        for zombie in self.zombies:
            self.physics_engines.append(
                PhysicsEngineSimple(zombie, self.survive_scene.blocks)
            )

    def on_mouse_press(self, position, modifiers):
        self.scene.on_mouse_press(position, modifiers)

        if self.scene == self.editor_scene:
            if self.editor_scene.play_button.is_pressed(position):
                self.switch_to_survive_scene()
        elif self.scene == self.survive_scene:
            self.player.shoot_at(position)

    def on_key_press(self, symbol, modifiers):
        self.inputs.press(symbol)

    def on_key_release(self, symbol, modifiers):
        self.inputs.release(symbol)

    def on_mouse_motion(self, position):
        self.scene.on_mouse_motion(position)

    def on_mouse_drag(self, position, modifiers):
        if self.scene == self.editor_scene:
            self.editor_scene.on_mouse_drag(position, modifiers)
        elif self.scene == self.survive_scene:
            self.player.shoot_at(position)

    def on_mouse_release(self, position, modifiers):
        self.scene.on_mouse_release(position, modifiers)
