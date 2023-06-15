from pygame import Surface
from pygame.rect import Rect

from utils.Position import Position


class Object:
    def __init__(self, position: Position, surface: Surface, rect: Rect, update: bool, is_interactive: bool = False):
        self.position = position
        self.surface = surface
        self.rect = rect

        # to be uses for moving objects so they can be cleared
        self.previous_rect = rect

        self.update = update
        self.is_interactive = is_interactive

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
        new_rect.center = (new_position.x, new_position.y)
        self.previous_rect = self.rect
        self.rect = new_rect
        self.position = new_position

    def handle_key(self, event):
        pass

    def time_update(self):
        pass

    def get_rect_to_updated(self):
        if not self.is_interactive:
            return self.rect
        else:
            return self.previous_rect
