import dataclasses
import random
from typing import List

import numpy as np

from defs import number_of_mines
from utils.Index import Index


@dataclasses.dataclass
class Tile:
    type: str
    center: Index
    orientation: int


@dataclasses.dataclass
class Grid:
    def __init__(self, level):
        match level:
            case 'easy':
                self.mine_map = np.zeros((9, 9), int)
                self.difficulty = level
                self.display_map = np.zeros((9, 9), int)
            case 'medium':
                self.mine_map = np.zeros((16, 16), int)
                self.difficulty = level
                self.display_map = np.zeros((16, 16), int)
            case 'hard':
                self.mine_map = np.zeros((16, 30), int)
                self.difficulty = level
                self.display_map = np.zeros((16, 30), int)
            case 'expert':
                self.mine_map = np.zeros((16, 30), int)
                self.difficulty = level
                self.display_map = np.zeros((16, 30), int)
            case 'insane':
                self.mine_map = np.zeros((20, 32), int)
                self.difficulty = level
                self.display_map = np.zeros((20, 32), int)

        self.initialize_mines()
        self.initialize_board()

    def initialize_mines(self):
        # find the number of mines to initialize
        mine_number = number_of_mines[self.difficulty]
        mine_indexes = []
        while len(mine_indexes) < mine_number:
            num_x = random.randint(0, len(self.mine_map[0]) - 1)
            num_y = random.randint(0, len(self.mine_map) - 1)
            if (num_x, num_y) not in mine_indexes:
                mine_indexes.append((num_x, num_y))
        for i in mine_indexes:
            self.mine_map[i[1]][i[0]] = 1

    def initialize_board(self):
        for y in range(len(self.mine_map)):
            for x in range(len(self.mine_map[0])):
                self.display_map[y][x] = self.count_mines(Index(x=x, y=y))

    def count_mines(self, index: Index):
        if index.y - 1 < 0:
            y_range = (0, index.y + 2)
        elif index.y + 1 > len(self.mine_map) - 1:
            y_range = (index.y - 1, len(self.mine_map) - 1)
        else:
            y_range = (index.y - 1, index.y + 2)

        if index.x - 1 < 0:
            x_range = (0, index.x + 2)
        elif index.x + 1 > len(self.mine_map[0]) - 1:
            x_range = (index.x - 1, len(self.mine_map[0]) - 1)
        else:
            x_range = (index.x - 1, index.x + 2)

        mine_count = 0
        for y in range(y_range[0], y_range[1]):
            for x in range(x_range[0], x_range[1]):
                if (x == index.x) and (y == index.y) and (self.mine_map[y][x] == 1):
                    mine_count = -1
                    return mine_count
                elif self.mine_map[y][x] == 1:
                    mine_count += 1
        return mine_count


if __name__ == '__main__':
    a = Grid(level='hard')
    print(a.display_map)
