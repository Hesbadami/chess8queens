import numpy as np


class Queen:
    def __init__(self, position):
        self.position = position
        self.board = np.arange(64)
        self.board = self.board.reshape(8, 8)

    def moves(self):
        position = self.position
        board = self.board
        legal = []

        for i in range(1, 8):
            diag_m = position + 9*i

            if diag_m in board:
                if np.abs(
                    np.where(board == diag_m-9)[0][0] -
                    np.where(board == diag_m)[0][0]
                ) == 1:
                    legal.append(diag_m)
                else:
                    break

        for i in range(1, 8):
            diag_m = position - 9*i

            if diag_m in board:
                if np.abs(
                    np.where(board == diag_m+9)[0][0] -
                    np.where(board == diag_m)[0][0]
                ) == 1:
                    legal.append(diag_m)
                else:
                    break

        for i in range(1, 8):
            diag_o = position + 7*i

            if diag_o in board:
                if np.abs(
                    np.where(board == diag_o-7)[0][0] -
                    np.where(board == diag_o)[0][0]
                ) == 1:
                    legal.append(diag_o)
                else:
                    break

        for i in range(1, 8):
            diag_o = position - 7*i

            if diag_o in board:
                if np.abs(
                    np.where(board == diag_o+7)[0][0] -
                    np.where(board == diag_o)[0][0]
                ) == 1:
                    legal.append(diag_o)
                else:
                    break

        for i in [x for x in range(-7, 8) if x != 0]:
            ver = position + 8*i

            if ver in board:
                legal.append(ver)

        for i in [x for x in range(-7, 8) if x != 0]:
            hor = position + i

            if hor in board[np.where(board == position)[0][0]]:
                legal.append(hor)

        return legal
