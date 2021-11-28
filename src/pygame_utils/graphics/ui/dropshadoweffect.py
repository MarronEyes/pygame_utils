import pygame
from graphics.ui.blur import Blur
from graphics.ui.effect import Effect
from graphics.ui.widget import Widget


class DropShadowEffect(Effect):

    def __init__(self, widget: Widget, color: pygame.Color = "black", offset: tuple = (5, 5), radius: int = 5):
        super().__init__(widget.rect.topleft, widget.rect.size, color, offset)

        self.radius = radius
        self.widget = widget
        self.surf = self.get_widget_surf()
        self.image = Blur.shadow(
            self.surf, radius, (self.color.r, self.color.g, self.color.b, self.color.a))

        self.rect = self.image.get_rect(topleft=widget.rect.topleft)
        self.update_offset()

    def get_widget_surf(self):
        s = pygame.Surface(self.screen.get_size()).convert_alpha()
        s.fill((0, 0, 0, 0))
        self.widget.render(s)

        ss = pygame.Surface(self.widget.rect.size).convert_alpha()
        ss.fill((0, 0, 0, 0))
        ss.blit(s, (-self.widget.rect.left, -self.widget.rect.top))

        return ss

    def set_size(self, size: tuple):
        self.image = pygame.transform.smoothscale(self.image, size)
        self.rect.size = size

    def set_color(self, color: pygame.Color):
        super().set_color(color)

        self.image = Blur.shadow(
            self.surf, self.radius, (self.color.r, self.color.g, self.color.b, self.color.a))
