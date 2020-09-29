# write your code here
class TicTacToe:
    def __init__(self):
        self.board = None
        self.create_board()

    def create_board(self):
        raw_cells = input("Enter cells:")
        # Exchange all "_" to " " symbols
        cells = [x.replace('_', ' ') for x in raw_cells]
        board = [(1, 3), cells[0], (2, 3), cells[1], (3, 3), cells[2],
                 (1, 2), cells[3], (2, 2), cells[4], (3, 2), cells[5],
                 (1, 1), cells[6], (2, 1), cells[7], (3, 1), cells[8]]
        self.board = board
        self.draw_board()
        self.menu()

    def draw_board(self):
        print(f"""---------
| {self.board[1]} {self.board[3]} {self.board[5]} |
| {self.board[7]} {self.board[9]} {self.board[11]} |
| {self.board[13]} {self.board[15]} {self.board[17]} |
---------""")

    def check_coord(self, x, y):
        if x.isalpha() or y.isalpha():
            print('You should enter numbers!')
            self.menu()
        elif int(x) > 3 or int(y) > 3:
            print('Coordinates should be from 1 to 3!')
            self.menu()
        elif self.board[self.board.index((int(x), int(y))) + 1] != ' ':
            print("This cell is occupied! Choose another one!")
            self.menu()

    def check_position(self, x, y):
        sign = 'X'
        if self.board.count('X') > self.board.count('O'):
            sign = 'O'

        self.board[self.board.index((x, y)) + 1] = sign

        if self.board[1] == self.board[3] == self.board[5] != ' ' or \
                self.board[7] == self.board[9] == self.board[11] != ' ' or \
                self.board[13] == self.board[15] == self.board[17] != ' ' or \
                self.board[1] == self.board[7] == self.board[13] != ' ' or \
                self.board[3] == self.board[9] == self.board[15] != ' ' or \
                self.board[5] == self.board[11] == self.board[17] != ' ' or \
                self.board[1] == self.board[9] == self.board[17] != ' ' or \
                self.board[5] == self.board[9] == self.board[13] != ' ':
            self.draw_board()
            print(f'{sign} wins')
        elif ' ' not in self.board:
            self.draw_board()
            print('Draw')
        else:
            self.draw_board()
            print('Game not finished')

        # Exit the game at 1/5 stage
        quit()

    def menu(self):
        coord = input("Enter the coordinates:").split()
        try:
            x, y = coord
            self.check_coord(x, y)
            self.check_position(int(x), int(y))
        except ValueError as e:
            print('You should enter numbers!')
            self.menu()


if __name__ == '__main__':
    game = TicTacToe()
