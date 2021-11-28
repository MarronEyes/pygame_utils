import pygame
from PIL import Image, ImageFilter


class Blur:

    @classmethod
    def blur_surface(cls, surf: pygame.Surface) -> pygame.Surface:
        pass

    @classmethod
    def shadow(cls, surf: pygame.Surface, radius: int = 3, color: tuple = (0, 0, 0)) -> pygame.Surface:
        img = cls.surf_to_img(surf)

        shadow_size = (img.width + radius * 5, img.height + radius * 5)
        back = Image.new(
            "RGBA", shadow_size, (0, 0, 0, 0)
        )

        shadow_pos = (
            back.width // 2 - img.width // 2,
            back.height // 2 - img.height // 2
        )

        back.paste(
            img,
            [
                shadow_pos[0],
                shadow_pos[1],
                shadow_pos[0] + img.size[0],
                shadow_pos[1] + img.size[1]
            ]
        )

        back = back.filter(ImageFilter.GaussianBlur(radius=radius))

        surf = cls.img_to_surf(back)
        return surf

    @classmethod
    def img_to_surf(cls, image: Image.Image) -> pygame.Surface:
        return pygame.image.fromstring(
            image.tobytes(),
            image.size,
            "RGBA"
        ).convert_alpha()

    @classmethod
    def surf_to_img(cls, surf: pygame.Surface) -> Image.Image:
        return Image.frombytes(
            "RGBA",
            surf.get_size(),
            pygame.image.tostring(surf, "RGBA", False)
        )
