# tic-tac-toe v 0.1
# based on https://geekflare.com/tic-tac-toe-python-code/
# and https://github.com/Cledersonbc/tic-tac-toe-minimax
import random
import time
from math import inf as infinity
from random import choice

PLAYER = -1
CPU = +1


class TicTacToe:

    @classmethod
    def get_random_first_player(cls):
        return random.randint(0, 1)

    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

    def get_empty_cells(self):
        cells = []

        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def is_won(self, player):
        win_state = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False

    def is_game_over(self):
        return self.is_won(PLAYER) or self.is_won(CPU)

    def render(self, cpu_sign, player_sign):

        chars = {
            -1: player_sign,
            +1: cpu_sign,
            0: ' '
        }
        str_line = '---------------'

        print('\n' + str_line)
        for row in self.board:
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)

    def evaluate(self):
        if self.is_won(CPU):
            score = +1
        elif self.is_won(PLAYER):
            score = -1
        else:
            score = 0

        return score

    def valid_move(self, x, y):
        if [x, y] in self.get_empty_cells():
            return True
        else:
            return False

    def set_move(self, x, y, player):
        if self.valid_move(x, y):
            self.board[x][y] = player
            return True
        else:
            return False

    def minimax(self, depth, player):
        if player == CPU:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.is_game_over():
            score = self.evaluate()
            return [-1, -1, score]

        for cell in self.get_empty_cells():
            x, y = cell[0], cell[1]
            self.board[x][y] = player
            score = self.minimax(depth - 1, -player)
            self.board[x][y] = 0
            score[0], score[1] = x, y

            if player == CPU:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def ai_turn(self, cpu_sign, player_sign):
        depth = len(self.get_empty_cells())
        if depth == 0 or self.is_game_over():
            return

        print(f'CPU turn [{cpu_sign}]')
        self.render(cpu_sign, player_sign)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(depth, CPU)
            x, y = move[0], move[1]

        self.set_move(x, y, CPU)
        time.sleep(1)

    def human_turn(self, cpu_sign, player_sign):
        depth = len(self.get_empty_cells())
        if depth == 0 or self.is_game_over():
            return

        row = -1
        col = -1

        print(f'Player turn [{player_sign}]')
        self.render(cpu_sign, player_sign)

        while (row < 1 or row > 3) and (col < 1 or col > 3):
            try:
                move = input("Enter row and column numbers: ")
                row, col = list(map(int, move.split()))

                if (row < 1 or row > 3) or (col < 1 or col > 3):
                    print('Enter values between 1 and 3')
                    row = -1
                    col = -1

                else:
                    can_move = self.set_move(row - 1, col - 1, PLAYER)
                    if not can_move:
                        print('This cell is not empty')
                        row = -1
                        col = -1
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Enter two int values between 1 and 3')

    def start(self):

        # 1 - Player gets the first turn, 0 - CPU gets it
        first = self.get_random_first_player()

        player_sign = 'X'
        cpu_sign = 'O'

        while len(self.get_empty_cells()) > 0 and not self.is_game_over():

            if first == 1:
                print("CPU gets first turn")
                self.ai_turn(cpu_sign, player_sign)
                first = None
            else:
                print("Player gets first turn")

            self.human_turn(cpu_sign, player_sign)
            self.ai_turn(cpu_sign, player_sign)

        # Game over message
        self.render(cpu_sign, player_sign)
        if self.is_won(PLAYER):
            print('HUMAN WIN!')
        elif self.is_won(CPU):
            print('CPU WIN!')
        else:
            print('DRAW!')


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
