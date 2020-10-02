import random


class TicTacToe:
    def __init__(self):
        # Create empty board when the game starts
        self.board = self.create_board()
        # self.create_board([' ' for _ in range(9)])
        # Store current move ('X' or 'O') turn to action
        self.menu()
        self.player1 = None
        self.player2 = None
        self.current_move = None

    def create_board(self):
        empty_cells = [' ' for _ in range(9)]
        # Use coordinate index - 1 for access to the cell
        board = [(1, 3), empty_cells[0], (2, 3), empty_cells[1], (3, 3), empty_cells[2],
                 (1, 2), empty_cells[3], (2, 2), empty_cells[4], (3, 2), empty_cells[5],
                 (1, 1), empty_cells[6], (2, 1), empty_cells[7], (3, 1), empty_cells[8]]
        return board

    def draw_board(self):
        print(f"""---------
| {self.board[1]} {self.board[3]} {self.board[5]} |
| {self.board[7]} {self.board[9]} {self.board[11]} |
| {self.board[13]} {self.board[15]} {self.board[17]} |
---------""")

    # Check if entered coordinate is right
    def check_coord(self, x, y):
        msg = None
        if self.check_position() is None:
            if x.isalpha() or y.isalpha():
                msg = 'You should enter numbers!'
            elif int(x) > 3 or int(y) > 3:
                msg = 'Coordinates should be from 1 to 3!'
            elif self.board[self.board.index((int(x), int(y))) + 1] != ' ':
                msg = "This cell is occupied! Choose another one!"
        else:
            print(self.check_position())
            self.menu()
        return msg

    def check_position(self):
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
        if self.check_position() is None:
            for i in self.board:
                if i == ' ':
                    self.board[self.board.index(i)] = self.current_move
                    print('Making move level "easy"')
                    self.draw_board()
                    self.change_move_state()
                    self.play_with_easy_pc()
        else:
            self.change_move_state()
            print(self.check_position())
            self.board = self.create_board()
            self.menu()

    def make_move(self, x, y):
        self.board[self.board.index((x, y)) + 1] = self.current_move

    def play_with_easy_pc(self):

        coord = input("Enter the coordinates:").split()
        x, y = coord

        if self.check_coord(x, y) is None:
            if self.check_position() is None:
                self.make_move(int(x), int(y))
                self.draw_board()
                self.change_move_state()
                self.easy_level()
            else:
                print(self.check_position())
                self.board = self.create_board()
                self.menu()
        else:
            print(self.check_coord(x, y))
            self.play_with_easy_pc()

    def user_user(self):

        coord_user1 = input("Enter the coordinates:").split()
        x1, y1 = coord_user1
        self.check_coord(x1, y1)
        self.make_move(int(x1), int(y1))
        self.draw_board()
        if self.check_position() is None:
            self.check_position()
        else:
            print(self.check_position())
            self.board = self.create_board()
            self.menu()
        self.change_move_state()

        coord_user2 = input("Enter the coordinates:").split()
        x2, y2 = coord_user2
        self.check_coord(x2, y2)
        self.make_move(int(x2), int(y2))
        self.draw_board()
        if self.check_position() is None:
            self.check_position()
        else:
            print(self.check_position())
            self.board = self.create_board()
            self.menu()
        self.change_move_state()

        self.user_user()

    def change_move_state(self):
        if self.current_move == 'X':
            self.current_move = 'O'
        else:
            self.current_move = 'X'

    def easy_easy(self):
        x, y = 0, 0
        for i in self.board:
            if i == " ":
                x, y = self.board[self.board.index(i) - 1]

        if self.check_position() is None:
            self.draw_board()
            self.board[self.board.index((x, y)) + 1] = self.current_move
            print('Making move level "easy"')
            self.change_move_state()
            self.easy_easy()
        else:
            self.change_move_state()
            self.draw_board()
            print(self.check_position())
            self.board = self.create_board()
            self.menu()

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
                self.current_move = 'X'
                self.easy_easy()
            elif command == ['start', 'user', 'easy']:
                self.player1, self.player2 = command[1], command[2]
                self.draw_board()
                self.current_move = 'X'
                self.play_with_easy_pc()
            elif command == ['start', 'user', 'user']:
                self.current_move = 'X'
                self.draw_board()
                self.user_user()
            else:
                print("Else statement fom menu works")


if __name__ == '__main__':
    game = TicTacToe()
