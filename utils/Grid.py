import dataclasses
import random

import numpy as np


@dataclasses.dataclass
class Grid:
    def __init__(self):
        self.arr = np.zeros((22, 10), int)
        self.lost = False

    def spawn(self):
        """
        spawns a random piece at the top
        :return:
        """
        piece = random.randint(0, 6)
        updated_arr = self.arr.copy()
        match piece:
            # square piece
            case 0:
                if (updated_arr[0][4] == 1) or (updated_arr[0][5] == 1) \
                        or (updated_arr[1][4] == 1) or (updated_arr[1][5] == 1):
                    self.lost = True
                else:
                    updated_arr[0][4] = 2
                    updated_arr[0][5] = 2
                    updated_arr[1][4] = 2
                    updated_arr[1][5] = 2
            # line piece
            case 1:
                if (updated_arr[0][4] == 1) or (updated_arr[0][5] == 1) \
                        or (updated_arr[0][3] == 1) or (updated_arr[0][6] == 1):
                    self.lost = True
                else:
                    updated_arr[0][3] = 2
                    updated_arr[0][5] = 2
                    updated_arr[0][4] = 2
                    updated_arr[0][6] = 2
            # S piece
            case 2:
                if (updated_arr[0][5] == 1) or (updated_arr[0][6] == 1) \
                        or (updated_arr[1][4] == 1) or (updated_arr[1][5] == 1):
                    self.lost = True
                else:
                    updated_arr[0][5] = 2
                    updated_arr[0][6] = 2
                    updated_arr[1][4] = 2
                    updated_arr[1][5] = 2
            # reverse s piece
            case 3:
                if (updated_arr[0][4] == 1) or (updated_arr[0][5] == 1) \
                        or (updated_arr[1][5] == 1) or (updated_arr[1][6] == 1):
                    self.lost = True
                else:
                    updated_arr[0][4] = 2
                    updated_arr[0][5] = 2
                    updated_arr[1][5] = 2
                    updated_arr[1][6] = 2
            # T piece
            case 4:
                if (updated_arr[0][4] == 1) or (updated_arr[0][5] == 1) \
                        or (updated_arr[0][6] == 1) or (updated_arr[1][5] == 1):
                    self.lost = True
                else:
                    updated_arr[0][4] = 2
                    updated_arr[0][5] = 2
                    updated_arr[0][6] = 2
                    updated_arr[1][5] = 2
            # L piece
            case 5:
                if (updated_arr[0][6] == 1) or (updated_arr[1][4] == 1) \
                        or (updated_arr[1][5] == 1) or (updated_arr[1][6] == 1):
                    self.lost = True
                else:
                    updated_arr[0][6] = 2
                    updated_arr[1][4] = 2
                    updated_arr[1][5] = 2
                    updated_arr[1][6] = 2
            # J piece
            case 6:
                if (updated_arr[0][4] == 1) or (updated_arr[1][4] == 1) \
                        or (updated_arr[1][5] == 1) or (updated_arr[1][6] == 1):
                    self.lost = True
                else:
                    updated_arr[0][4] = 2
                    updated_arr[1][4] = 2
                    updated_arr[1][5] = 2
                    updated_arr[1][6] = 2
        self.arr = updated_arr

    def update(self):
        """
        Handles the movement of the piece down, will move down the piece by 1 tile on the array
        :return:
        """
        updated_arr = self.arr.copy()
        indices = np.unique(np.where(updated_arr == 2)[0])
        for index_y in reversed(indices):
            for index_x, element in enumerate(updated_arr[index_y]):
                if element == 2:
                    if (index_y >= 20) or (updated_arr[index_y + 1][index_x] == 1):
                        self.arr = np.where(self.arr == 2, 1, self.arr)
                        return
                    else:
                        updated_arr[index_y + 1][index_x] = 2
                        updated_arr[index_y][index_x] = 0
        self.arr = updated_arr


if __name__ == '__main__':
    a = Grid()
    a.spawn()
    print(a.arr)
    a.update()
    print(a.arr)
