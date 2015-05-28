from game import State


class UserInterface:
    def __init__(self, game):
        self.game = game

    def print_board(self):
        width, height = self.game.dimensions()
        print('─' * (width * 4 + 1))
        for y in range(height):
            print('│ ', end='')
            for x in range(width):
                if self.game.is_opened((x, y)):
                    print(
                        self.game.value_at_position((x, y)) or ' ',
                        end=' │ ')
                elif self.game.is_flagged((x, y)):
                    print('⚑', end=' │ ')
                else:
                    print('█', end=' │ ')
            print()
            print('─' * (width * 4 + 1))

    def parse_input(self, command):
        if command == 'quit':
            self.game.state = State.quit
            return

        action, *position = command.split()
        position = tuple(map(int, position))

        if action == 'open':
            self.game.open_position(position)
        elif action == 'flag':
            self.game.flag_position(position)
        elif action == 'neighbours':
            self.game.open_neighbours(position)

    def main_loop(self):
        self.print_board()
        while self.game.state is State.running:
            self.parse_input(input('move: '))
            self.print_board()

        if self.game.state is State.lost:
            print(':(')
        elif self.game.state is State.won:
            print(':) CONGRATS!')
        else:
            print('QUITTER!')
