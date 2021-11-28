import pygame
import pygame.display
import pygame.time
import pygame.event


class Window:

    DEFAULT_WINDOW_TITLE = "pygame window"
    DEFAULT_WINDOW_SIZE = (800, 450)
    DEFAULT_WINDOW_COLOR = "black"
    DEFAULT_FPS = 60

    def __init__(self, title: str = DEFAULT_WINDOW_TITLE, size: tuple = DEFAULT_WINDOW_SIZE, background_color: pygame.Color = DEFAULT_WINDOW_COLOR, fps: int = DEFAULT_FPS):
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.bg_color = background_color
        self.running = True

    def handle_event(self, event: pygame.event.Event):
        """Override this method"""
        pass

    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.handle_event(event)

            self.update()
            self.update_window()

        self.quit()

    def quit(self):
        self.running = False
        pygame.quit()

    def update(self):
        """Override this method"""
        pass

    def update_window(self):
        if self.bg_color:
            self.screen.fill(self.bg_color)
        self.render()
        pygame.display.update()
        self.clock.tick(self.fps)

    def render(self):
        """Override this method"""
        pass
