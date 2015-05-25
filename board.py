from enum import Enum
from itertools import product
from random import randint


class Cell(Enum):
    mine = '*'
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nothing = 0


class Board:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.mines = set()
        self.flagged = set()
        self.opened = set()

    def __getitem__(self, position):

        if position in self.mines:
            return Cell.mine

        return Cell(len(
            self.neighbours_of(position) & self.mines))

    def neighbours_of(self, position):
        return {
            (offset[0] + position[0], offset[1] + position[1])
            for offset in product(range(-1, 2), range(-1, 2))
        }

    def flagged_neighbours(self, position):
        return len(self.neighbours_of(position) & self.flagged)

    def open_position(self, position):
        self.opened.add(position)

    def is_opened(self, position):
        return position in self.opened

    def flag_position(self, position):
        self.flagged.add(position)

    def is_flagged(self, position):
        return position in self.flagged

    def generate(self, percent):
        for x in range(self.width):
            for y in range(self.height):
                if randint(1, 100/percent) == 1:
                    self.mines.add((x, y))
