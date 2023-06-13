from pygame import Surface
from pygame.rect import Rect

from utils.Position import Position


class Object:
    def __init__(self, position: Position, surface: Surface, rect: Rect, update: bool):
        self.position = position
        self.surface = surface
        self.rect = rect
        self.update = update

    def update_rect_same_position(self) -> None:
        """
        Note: assumes that surface has been updated
        """
        new_rect = self.surface.get_rect()
        new_rect.x = self.position.x
        new_rect.y = self.position.y

        self.rect = new_rect

    def update_rect_new_position(self, new_position: Position) -> None:
        """
        Note: assumes that surface has been updated
        """
        new_rect = self.surface.get_rect()
        new_rect.x = new_position.x
        new_rect.y = new_position.y

        self.rect = new_rect

    def handle_key(self, key):
        raise NotImplemented()
