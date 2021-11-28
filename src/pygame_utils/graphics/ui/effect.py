import pygame
from graphics.component import Component


class Effect(Component):

    def __init__(self, pos: tuple, size: tuple, color: pygame.Color = "black", offset: tuple = (5, 5)) -> None:
        super().__init__()

        self.color = pygame.Color(color)
        self.offset = offset
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=pos)
        self.update_offset()

    def set_color(self, color: pygame.Color):
        self.color = pygame.Color(color)

    def set_offset(self, offset: tuple):
        self.offset = offset
        self.update_offset()

    def update_pos(self, pos: tuple):
        self.rect.topleft = pos
        self.update_offset()

    def update_offset(self):
        pos = (self.rect.left + self.offset[0], self.rect.top + self.offset[1])
        self.rect.topleft = pos

    def render(self, surf: pygame.Surface = None):
        if surf is None:
            surf = self.screen

        surf.blit(self.image, self.rect)
