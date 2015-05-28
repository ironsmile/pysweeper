from board import Board
from game import Game, State
from tui import UserInterface

board = Board(10, 10)
board.generate(20)

game = Game(board)
ui = UserInterface(game)

ui.print_board()
while game.state is State.running:
    ui.parse_input(input('move: '))
    ui.print_board()

if game.state is State.lost:
    print(':(')
elif game.state is State.won:
    print(':) CONGRATS!')
else:
    print('QUITTER!')
