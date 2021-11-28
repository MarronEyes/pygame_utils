import pygame
from graphics.ui.widget import Widget
from graphics.ui.dropshadoweffect import DropShadowEffect


class Label(Widget):

    def __init__(
            self,
            text: str,
            pos: tuple,
            font: pygame.font.Font,
            antialaising: bool = False,
            text_color: pygame.Color = "black",
            background_color: pygame.Color = None,
            shadow: bool = False,
            shadow_offset = (10, 10),
            shadow_radius: int = 5
        ):
        super().__init__(pos, font.size(text))

        self.font = font

        self.text = text
        self.aa = antialaising
        self.color = text_color
        self.bg_color = background_color

        self.image = self.font.render(text, self.aa, self.color, self.bg_color)
        self.rect = self.image.get_rect(center=pos)
        self.shadow = None
        if shadow:
            self.shadow = DropShadowEffect(
                self, offset=shadow_offset, radius=shadow_radius)

    def set_pos(self, pos: tuple):
        self.rect.topleft = pos
        if self.shadow:
            self.shadow.update_pos(pos)

    def set_center(self, center: tuple):
        self.rect.center = center
        self.shadow.update_pos(self.rect.topleft)

    def set_text(self, text: str):
        self.text = text
        self.update_text()

    def set_color(self, color):
        self.color = color
        self.update_text()

    def set_background_color(self, bg_color):
        self.bg_color = bg_color
        self.update_text()

    def set_antialaising(self, aa: bool):
        self.aa = aa
        self.update_text()

    def update_text(self):
        self.image = self.font.render(
            self.text, self.aa, self.color, self.bg_color)
        self.rect.size = self.image.get_size()

    def render(self, surf: pygame.Surface = None):
        if surf is None:
            surf = self.screen

        if self.shadow:
            self.shadow.render(surf)
        surf.blit(self.image, self.rect)
