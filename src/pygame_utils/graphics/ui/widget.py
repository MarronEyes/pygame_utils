import pygame
from graphics.component import Component


class Widget(Component):

    def __init__(self, pos: tuple, size: tuple) -> None:
        super().__init__()
        self.collided = False
        self.clicked = False

        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        self.check()

    def render(self, surf: pygame.Surface = None):
        if surf is None:
            surf = self.screen

        surf.blit(self.image, self.rect)

    def on_click_down(self):
        pass

    def on_click_up(self):
        pass

    def on_hover_enter(self):
        pass

    def on_hover_quit(self):
        pass

    def check(self):
        pos = pygame.mouse.get_pos()
        state = pygame.mouse.get_pressed()
        if self.rect.collidepoint(pos):

            if state[0] and not self.clicked and self.collided:
                self.on_click_down()
                self.clicked = True

            if not self.collided:
                self.on_hover_enter()
                self.collided = True

            if not state[0] and self.clicked:
                self.on_click_up()
                self.clicked = False

        elif self.collided:
            self.collided = False
            self.clicked = False
            self.on_hover_quit()
