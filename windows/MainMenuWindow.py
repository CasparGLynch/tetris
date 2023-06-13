# Python
from typing import List

# Pygame
import pygame
from pygame.event import Event

# Tetris
import defs
from defs import screen_width, screen_height
from objects.Object import Object
from objects.TextBoxObject import TextBoxObject
from utils.Position import Position
from windows.Window import Window


class MainMenuWindow(Window):

    def __init__(self):
        super().__init__()

        main_menu = TextBoxObject(
            position=Position(x=screen_width//2, y=screen_height//2),
            text='Press Enter to Play!',
            size=23,
            center=True
        )
        self.screen_rects.append(main_menu)

    def key_updates(self, event: Event):
        # check for the rects on screem
        objects_to_update = [_rect for _rect in self.screen_rects if _rect.is_interactive]
        for _object in objects_to_update:
            _object.handle_key(Event)

        # window specific updates
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return defs.SWITCH_TO_GAME

    def time_updates(self):
        pass

    def display(self) -> List[Object]:
        to_be_updated = [x for x in self.screen_rects if x.update]
        for i in self.screen_rects:
            i.update = False
        return to_be_updated
