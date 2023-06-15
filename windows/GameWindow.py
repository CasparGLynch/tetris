from typing import List

import pygame.image
from pygame.event import Event

import defs
from objects.Object import Object
from objects.Player import Player
from windows.Window import Window


class GameWindow(Window):

    def __init__(self):
        super().__init__()
        background = pygame.image.load('assets/backgrounds/level1.jpg')
        self.background = pygame.transform.scale(background, (defs.screen_width, defs.screen_height))
        main_menu = Player(position=None, center=True)
        self.screen_rects.append(main_menu)

    def key_updates(self, event: Event):
        objects_to_update = [_rect for _rect in self.screen_rects if _rect.is_interactive]
        for _object in objects_to_update:
            _object.handle_key(event)

        return 0

    def time_updates(self):
        objects_to_update = [_rect for _rect in self.screen_rects if _rect.is_interactive]
        for _object in objects_to_update:
            _object.time_update()

        return 0

    def display(self) -> List[Object]:
        to_be_updated = [x for x in self.screen_rects if x.update]
        for i in self.screen_rects:
            i.update = False
        return to_be_updated

