# tic-tac-toe v 0.1
# based on https://geekflare.com/tic-tac-toe-python-code/
# and https://github.com/Cledersonbc/tic-tac-toe-minimax

import random


class TicTacToe:

    @classmethod
    def get_random_first_player(cls):
        return random.randint(0, 1)

    @classmethod
    def swap_player_turn(cls, player):
        return 'X' if player == 'O' else 'O'

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def is_input_correct(self, row, col):
        if (row > len(self.board)) or (row < 1):
            return False
        elif (col > len(self.board[0])) or (col < 1):
            return False
        return True

    def start(self):
        self.create_board()

        # O is always the computer
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()
            entered_value = ""

            # taking user input
            try:
                entered_value = input("Enter row and column numbers to fix spot: ")
                entered_values = entered_value.split()
                row, col = list(map(int, entered_values))
                if not self.is_input_correct(row, col):
                    raise ValueError("Column or row number is incorrect")
            except Exception as e:
                print(f"Input {entered_value} has failed: reason: {e}")
                continue

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


if __name__ == '__main__':
    # starting the game
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()

# TODO:
# 2. Добавить ИИ, нолик - всегда комп
