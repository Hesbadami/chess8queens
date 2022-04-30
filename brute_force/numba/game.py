import numpy as np
import numba
from time import time

rng = np.random.default_rng()
qq = "♕"
sq = "□"


def printboard(positions):
    beard = np.arange(64)
    beard = beard.astype('U')
    for i in range(64):
        beard[i] = sq
    for i in positions:
        beard[i] = qq
    board = beard.reshape(8, 8)
    for i in range(8):
        print(
            board[i][0]+"\t",
            board[i][1]+"\t",
            board[i][2]+"\t",
            board[i][3]+"\t",
            board[i][4]+"\t",
            board[i][5]+"\t",
            board[i][6]+"\t",
            board[i][7]
        )
        print("\n")


pt1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0]])


@numba.jit("i8[:](i8[:,:])", nopython=True, nogil=True)
def game(pt1):
    tr = 0
    truce = False
    beard = np.arange(64)

    while not truce:
        positions = np.random.choice(beard, 8, replace=False)
        ini = True
        for row in pt1:
            if (positions == row).all():
                ini = False
        if ini:
            tr += 1
            if tr % 100 == 0:
                print(tr)

            # positions = np.array([5, 11, 16, 28, 39, 41, 54, 58])
            legals = []
            board = beard.reshape(8, 8)

            for position in positions:
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
                legals.extend(legal)

            if len(set(positions).intersection(set(legals))) == 0:
                truce = True

            pt2 = np.arange((tr+1)*8).reshape(tr+1, 8)
            pt2[:tr] = pt1.copy()
            pt2[-1] = positions
            pt1 = pt2.copy()

    return positions


a = time()
printboard(game(pt1))
b = time()

print("Time: ", round(b-a, 2), "Seconds")
