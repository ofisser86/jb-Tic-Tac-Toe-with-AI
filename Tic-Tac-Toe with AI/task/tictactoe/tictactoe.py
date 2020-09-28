# write your code here
class TicTacToe:
    def __init__(self):
        self.board = None
        self.draw_field()

    def draw_field(self):
        cell = input('Enter cells:')
        cells = [x.replace('_', ' ') for x in cell]
        board = [[(1, 3, cells[0]), (2, 3, cells[1]), (3, 3, cells[2])],
                 [(1, 2, cells[3]), (2, 2, cells[4]), (3, 2, cells[5])],
                 [(1, 1, cells[6]), (2, 1, cells[7]), (3, 1, cells[8])]]


        print(board[1][1])

        print("---------")
        for i in board:
            print('|', end=" ")
            for j in i:
                print(f"{j[2]}", end=" ")
            print("|")
        print("---------")

        self.board = board
        self.menu()

    def check_coord(self, x, y):
        if x.isalpha() or y.isalpha():
            print('You should enter numbers!')
            self.menu()
        elif int(x) > 3 or int(y) > 3:
            print('Coordinates should be from 1 to 3!')
            self.menu()

    def check_position(self, x, y):
        if self.board[x][y] == ' ':
            return True
        else:
            return False

    def menu(self):
        coord = input("Enter the coordinates:").split()
        x, y = coord
        self.check_coord(x, y)

        self.check_position(int(x), int(y))


if __name__ == '__main__':
    game = TicTacToe()
