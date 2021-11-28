import pygame


class Group(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

    def handle_event(self, event: pygame.event.Event):
        for component in self.sprites():
            component.handle_event(event)

    def draw(self, surface: pygame.Surface) -> None:
        for component in self.sprites():
            component.render(surface)
