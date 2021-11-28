import pygame


class Scene:

    def __init__(self, scene_manager, game):
        self.screen = pygame.display.get_surface()
        self.scene_manager = scene_manager
        self.game = game

    def on_scene_enter(self):
        pass

    def on_scene_quit(self):
        pass

    def handle_event(self, event: pygame.event.Event):
        pass

    def update(self):
        pass

    def render(self):
        pass
