import unittest
from board import Board, Cell


class TestBoard(unittest.TestCase):
    def test_get_mine(self):
        board = Board(10, 10)
        board.mines.add((4, 4))
        self.assertEqual(board[4, 4], Cell.mine)

    def test_get_not_a_mine(self):
        board = Board(10, 10)
        self.assertEqual(board[4, 4], Cell.nothing)

    def test_count_mines(self):
        board = Board(3, 3)
        board.mines.add((0, 0))
        board.mines.add((1, 0))
        self.assertEqual(board[0, 1], Cell.two)
        self.assertEqual(board[1, 1], Cell.two)
        self.assertEqual(board[2, 0], Cell.one)

    def test_flagged_neighbours(self):
        board = Board(3, 3)
        board.flagged.add((0, 0))
        board.flagged.add((1, 0))
        self.assertEqual(board.flagged_neighbours((0, 1)), 2)
        self.assertEqual(board.flagged_neighbours((1, 1)), 2)
        self.assertEqual(board.flagged_neighbours((2, 0)), 1)


if __name__ == '__main__':
    unittest.main()
