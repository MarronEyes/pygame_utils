import pygame
from graphics.ui.widget import Widget
from graphics.ui.label import Label


class Entry(Widget):

    def __init__(
        self,
        pos: tuple,
        size: tuple,
        font: pygame.font.Font) -> None:
        super().__init__(pos, size)

        self.font = font
        # unicodes contains tuple of (letter, surface)
        self.unicodes = []
        self.index = 0
        self.text = ""

        self.focus = True

    def update_text(self):
        for letter in range(len(self.text)):
            if letter <= len(self.unicodes) - 1:
                if not self.unicodes[letter][2]:
                    l = self.font.render(self.text[letter], True, "black")
                    self.unicodes.append([self.text[letter], l, False])
            else:
                l = self.font.render(self.text[letter], True, "black")
                self.unicodes.append([self.text[letter], l, False])


    def on_click_up(self):
        print(self.text)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.update_text()

    def update(self):
        super().update()

    def render(self, surf: pygame.Surface = None):
        if surf is None:
            surf = self.screen

        pygame.draw.rect(surf, "black", self.rect, width=5)
