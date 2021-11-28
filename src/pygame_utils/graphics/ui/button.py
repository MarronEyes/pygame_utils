import pygame
from graphics.ui.widget import Widget
from graphics.ui.label import Label
from graphics.ui.dropshadoweffect import DropShadowEffect
from graphics.ui.animatedcolor import AnimatedColor
from graphics.renderer import Renderer


class Button(Widget):

    def __init__(
            self,
            pos: tuple,
            size: tuple,
            color: pygame.Color,
            hover_color: pygame.Color,
            click_color: pygame.Color,
            clock: pygame.time.Clock,
            text: str,
            font: pygame.font.Font,
            text_color: pygame.Color,
            shadow: bool = False,
            shadow_offset=(5, 5),
            shadow_radius: int = 5,
            border: int = 0,
            radius: int = -1,
            func=None):
        super().__init__(pos, size)

        self.border = border
        self.radius = radius
        self.colors = [color, hover_color, click_color]
        self.color = AnimatedColor(
            self.colors, 0.2, clock)
        self.text = Label(text, self.rect.center, font, True, text_color)

        self.func = func
        self.shadow = None
        if shadow:
            self.shadow = DropShadowEffect(
                self, offset=shadow_offset, radius=shadow_radius)

    def set_pos(self, pos: tuple):
        self.rect.topleft = pos
        self.text.set_center(self.rect.center)
        if self.shadow:
            self.shadow.update_pos(pos)

    def update(self):
        super().update()

        self.color.update()

    def render(self, surf: pygame.Surface = None):
        if surf is None:
            surf = self.screen

        if self.shadow:
            self.shadow.render(surf)

        Renderer.rect(surf, self.color.current_color, self.rect,
                      border_radius=self.radius, width=self.border)

        self.text.render(surf)

    def on_click_down(self):
        self.color.set_colors([self.color.current_color, self.colors[2]])

    def on_click_up(self):
        self.color.set_colors([self.color.current_color, self.colors[1]])
        if self.func:
            self.func()

    def on_hover_enter(self):
        self.color.set_colors([self.colors[0], self.colors[1]])

    def on_hover_quit(self):
        self.color.set_colors([self.color.current_color, self.colors[0]])
