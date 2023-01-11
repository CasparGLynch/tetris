from typing import List

from pygame.event import Event

from objects.Object import Object
from windows.Window import Window


class GameWindow(Window):

    def __init__(self):
        super().__init__()

    def key_updates(self, event: Event):
        pass

    def time_updates(self):
        pass

    def display(self) -> List[Object]:
        return self.to_be_updated
