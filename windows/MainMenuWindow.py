from typing import List

from pygame.event import Event

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
        self.to_be_updated.append(main_menu)

    def key_updates(self, event: Event):
        pass

    def time_updates(self):
        pass

    def display(self) -> List[Object]:
        return self.to_be_updated
