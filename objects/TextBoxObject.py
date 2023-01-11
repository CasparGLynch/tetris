import pygame.font
from pygame import Surface
from pygame.rect import Rect

from defs import text_color, game_font, screen_height, screen_width
from objects.Object import Object
from utils.Position import Position


class TextBoxObject(Object):
    def __init__(self, position: Position, text: str, size: int, center=False):
        self.font = pygame.font.Font(game_font, size)
        text_surface = self.font.render(text, True, text_color)
        text_rect = text_surface.get_rect()
        if center:
            text_rect.y = (screen_height // 2) - (text_rect.height // 2)
            text_rect.x = (screen_width // 2) - (text_rect.width // 2)
        else:
            text_rect.x = position.x
            text_rect.y = position.y

        super().__init__(position=position, surface=text_surface, rect=text_rect)

    def update_text(self, text: str):
        x = self.rect.x
        y = self.rect.y
        self.font = pygame.font.Font(game_font, 36)
        text_surface = self.font.render(text, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y

        self.rect = text_rect
        self.surface = text_surface
