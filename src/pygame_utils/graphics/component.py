import pygame


class Component(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self.screen = pygame.display.get_surface()

    def handle_event(self, event: pygame.event.Event):
        pass

    def update(self):
        pass

    def render(self, surf: pygame.Surface = None):
        pass
