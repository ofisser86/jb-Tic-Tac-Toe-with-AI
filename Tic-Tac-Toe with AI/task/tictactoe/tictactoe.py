import random


class TicTacToe:
    def __init__(self):
        # Create empty board when the game starts
        self.board = None
        self.create_board([' ' for _ in range(9)])
        # Store current move ('X' or 'O') turn to action
        self.menu()
        self.player1 = None
        self.player2 = None
        self.current_move = None

    def create_board(self, empty_cells):
        # Use coordinate index - 1 for access to the cell
        board = [(1, 3), empty_cells[0], (2, 3), empty_cells[1], (3, 3), empty_cells[2],
                 (1, 2), empty_cells[3], (2, 2), empty_cells[4], (3, 2), empty_cells[5],
                 (1, 1), empty_cells[6], (2, 1), empty_cells[7], (3, 1), empty_cells[8]]
        self.board = board

    def draw_board(self):
        print(f"""---------
| {self.board[1]} {self.board[3]} {self.board[5]} |
| {self.board[7]} {self.board[9]} {self.board[11]} |
| {self.board[13]} {self.board[15]} {self.board[17]} |
---------""")

    # Check if entered coordinate is right
    def check_coord(self, x, y):
        msg = None
        if x.isalpha() or y.isalpha():
            msg = 'You should enter numbers!'
        elif int(x) > 3 or int(y) > 3:
            msg = 'Coordinates should be from 1 to 3!'
        elif self.board[self.board.index((int(x), int(y))) + 1] != ' ':
            msg = "This cell is occupied! Choose another one!"
        return msg

    def check_position(self, x, y):
        msg = None
        # All winning combinations

        if self.board[1] == self.board[3] == self.board[5] != ' ' or \
                self.board[7] == self.board[9] == self.board[11] != ' ' or \
                self.board[13] == self.board[15] == self.board[17] != ' ' or \
                self.board[1] == self.board[7] == self.board[13] != ' ' or \
                self.board[3] == self.board[9] == self.board[15] != ' ' or \
                self.board[5] == self.board[11] == self.board[17] != ' ' or \
                self.board[1] == self.board[9] == self.board[17] != ' ' or \
                self.board[5] == self.board[9] == self.board[13] != ' ':
            msg = f'{self.current_move} wins'
        elif ' ' not in self.board:
            msg = 'Draw'
        return msg

    # Easy game level - PC choose first empty cell (cell with "<space>")
    def easy_level(self):
        for i in self.board:
            if i == ' ':
                self.board[self.board.index(i)] = self.current_move
                print('Making move level "easy"')
                self.draw_board()
                self.current_move = 'O'
                self.play_with_easy_pc()

    def make_move(self, x, y):
        self.board[self.board.index((x, y)) + 1] = self.current_move

    def play_with_easy_pc(self):

        coord = input("Enter the coordinates:").split()
        x, y = coord

        if self.check_coord(x, y) is None:
            if self.check_position(int(x), int(y)) is None:
                self.make_move(int(x), int(y))
                self.draw_board()
                self.current_move = 'X'
                self.easy_level()
            else:
                print(self.check_position(int(x), int(y)))
                self.menu()
        else:
            print(self.check_coord(x, y))
            self.play_with_easy_pc()

    def user_user(self):
        ...

    def easy_easy(self):
        x = random.randint(1, 3)
        y = random.randint(1, 3)

        if self.current_move == 'X':
            self.current_move = 'O'
        else:
            self.current_move = 'X'

        if self.check_coord(str(x), str(y)) is None:
            if self.check_position(x, y) is None:
                self.draw_board()
                self.check_position(x, y)
                self.board[self.board.index((x, y)) + 1] = self.current_move
                print('Making move level "easy"')
                self.easy_easy()
            else:
                self.draw_board()
                print(self.check_position(x, y))
                self.menu()
        else:
            self.easy_easy()

    def menu(self):
        while True:
            command = input("Input command:").split()
            if command[0] == 'exit' and len(command) == 1:
                quit()
            elif len(command) != 3 or command[0] != 'start':
                print("Bad parameters!")
            elif command == ['start', 'easy', 'user']:
                self.draw_board()
                self.player1, self.player2 = command[1], command[2]
                self.current_move = 'X'
                self.easy_level()
            elif command == ['start', 'easy', 'easy']:
                self.player1, self.player2 = command[1], command[2]
                self.current_move = 'O'
                self.easy_easy()
            elif command == ['start', 'user', 'user']:
                ...


if __name__ == '__main__':
    game = TicTacToe()
