class TicTacToe:
    def __init__(self):
        self.board = None
        # Create empty board when the game starts
        self.create_board([' ' for _ in range(9)])
        # Store current move ('X' or 'O') turn to action
        self.current_move = None

    def create_board(self, empty_cells):
        # Use coordinate index - 1 for access to the cell
        board = [(1, 3), empty_cells[0], (2, 3), empty_cells[1], (3, 3), empty_cells[2],
                 (1, 2), empty_cells[3], (2, 2), empty_cells[4], (3, 2), empty_cells[5],
                 (1, 1), empty_cells[6], (2, 1), empty_cells[7], (3, 1), empty_cells[8]]
        self.board = board
        self.draw_board()
        self.menu()

    def draw_board(self):
        print(f"""---------
| {self.board[1]} {self.board[3]} {self.board[5]} |
| {self.board[7]} {self.board[9]} {self.board[11]} |
| {self.board[13]} {self.board[15]} {self.board[17]} |
---------""")

    # Check if entered coordinate is right
    # Todo: Improve DRY
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

        self.board[self.board.index((x, y)) + 1] = "X"
        self.current_move = 'X'
        # All winning combinations
        if self.board[1] == self.board[3] == self.board[5] != ' ' or \
                self.board[7] == self.board[9] == self.board[11] != ' ' or \
                self.board[13] == self.board[15] == self.board[17] != ' ' or \
                self.board[1] == self.board[7] == self.board[13] != ' ' or \
                self.board[3] == self.board[9] == self.board[15] != ' ' or \
                self.board[5] == self.board[11] == self.board[17] != ' ' or \
                self.board[1] == self.board[9] == self.board[17] != ' ' or \
                self.board[5] == self.board[9] == self.board[13] != ' ':
            self.draw_board()
            print(f'{self.current_move} wins')
        elif ' ' not in self.board:
            self.draw_board()
            print('Draw')
        else:
            self.draw_board()
            print('Making move level "easy"')
            # PC making a move
            self.easy_level()
            self.current_move = 'O'

        quit()

    # Easy game level - PC choose first empty cell (cell with "<space>")
    def easy_level(self):
        for i in self.board:
            if i == ' ':
                self.board[self.board.index(i)] = 'O'
                self.draw_board()
                self.menu()

    def menu(self):
        coord = input("Enter the coordinates:").split()
        try:
            x, y = coord
            self.check_coord(x, y)
            self.check_position(int(x), int(y))
        except ValueError:
            print('You should enter numbers!')
            self.menu()


if __name__ == '__main__':
    game = TicTacToe()
