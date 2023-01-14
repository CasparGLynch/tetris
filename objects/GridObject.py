from objects.Object import Object
from utils.Position import Position


class GridObject(Object):
    def __init__(self, position: Position, update: bool):



        super().__init__(position, surface, rect, update)
