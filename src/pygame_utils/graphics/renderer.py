import pygame
import pygame.gfxdraw


class Renderer:

    @classmethod
    def rounded_rect(cls, surface: pygame.Surface, rect: pygame.Rect, color: pygame.Color, radius: int = -1):
        if rect.width < 2 * radius or rect.height < 2 * radius:
            return

        pygame.gfxdraw.aacircle(surface, rect.left + radius,
                                rect.top + radius, radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right -
                                radius - 1, rect.top + radius, radius, color)
        pygame.gfxdraw.aacircle(surface, rect.left + radius,
                                rect.bottom - radius - 1, radius, color)
        pygame.gfxdraw.aacircle(surface, rect.right -
                                radius - 1, rect.bottom - radius - 1, radius, color)

        pygame.gfxdraw.filled_circle(
            surface, rect.left + radius, rect.top + radius, radius, color)
        pygame.gfxdraw.filled_circle(
            surface, rect.right - radius - 1, rect.top + radius, radius, color)
        pygame.gfxdraw.filled_circle(
            surface, rect.left + radius, rect.bottom - radius - 1, radius, color)
        pygame.gfxdraw.filled_circle(
            surface, rect.right - radius - 1, rect.bottom - radius - 1, radius, color)

        rect_tmp = pygame.Rect(rect)

        rect_tmp.width -= 2 * radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)

        rect_tmp.width = rect.width
        rect_tmp.height -= 2 * radius
        rect_tmp.center = rect.center
        pygame.draw.rect(surface, color, rect_tmp)

    @classmethod
    def rect(cls, surface: pygame.Surface, color: pygame.Color, rect: pygame.Rect, width: int = 0, border_radius: int = -1):
        rect = pygame.Rect(rect)
        color = pygame.Color(color)
        if width > 0:
            pygame.draw.rect(surface, color, rect, width=width, border_radius=border_radius)
        elif border_radius != -1:
            cls.rounded_rect(surface, rect, color, border_radius)
