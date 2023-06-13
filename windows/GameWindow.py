from typing import List

from pygame.event import Event

from defs import screen_width, screen_height
from objects.Object import Object
from objects.TextBoxObject import TextBoxObject
from utils.Position import Position
from windows.Window import Window


class GameWindow(Window):

    def __init__(self):
        super().__init__()
        main_menu = TextBoxObject(
            position=Position(x=screen_width // 2, y=screen_height // 2),
            text='You are Play ing~!!',
            size=23,
            center=True
        )
        self.screen_rects.append(main_menu)

    def key_updates(self, event: Event):
        pass

    def time_updates(self):
        pass

    def display(self) -> List[Object]:
        to_be_updated = [x for x in self.screen_rects if x.update]
        for i in self.screen_rects:
            i.update = False
        return to_be_updated

