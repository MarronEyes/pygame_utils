import pygame
from graphics.component import Component


class AnimatedColor(Component):

    def __init__(self, colors: list, duration: float, clock: pygame.time.Clock):
        super().__init__()
        self.colors = [pygame.Color(color) for color in colors]
        self.current_color = self.colors[0]

        self.clock = clock
        self.is_animating = False
        self.elapsed_time = 0
        self.duration = duration

    def set_colors(self, colors: list):
        self.colors = [pygame.Color(color) for color in colors]

        self.is_animating = True
        self.elapsed_time = 0

    def update(self):
        if self.is_animating:
            self.elapsed_time += self.clock.get_time() / 1000
            if self.elapsed_time < self.duration:
                self.current_color = [
                    x + (
                        (
                            (y - x) / self.duration
                        ) * self.elapsed_time
                    )
                    for x, y in zip(
                        *self.colors
                    )
                ]
            else:
                self.elapsed_time = 0
                self.is_animating = False
