from enum import Enum
from board import Cell


class State(Enum):
    running = 'running'
    won = 'won'
    lost = 'lost'
    quit = 'quit'


class Game:
    def __init__(self, board):
        self.board = board
        self.state = State.running

    def open_position(self, position):
        self.board.open_position(position)
        cell = self.board[position]
        if cell is Cell.mine:
            self.state = State.lost
            return

    def flag_position(self, position):
        self.board.flag_position(position)
