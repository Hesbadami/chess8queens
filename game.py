from peace import Queen
import numpy as np

qq = "♕"
sq = "□"


def printboard(board):
    for i in range(8):
        print(
            board[i][0],
            board[i][1],
            board[i][2],
            board[i][3],
            board[i][4],
            board[i][5],
            board[i][6],
            board[i][7]
        )


rng = np.random.default_rng()
truce = False
pt = []
tr = 0
while not(truce):
    positions = rng.choice(64, size=8, replace=False)
    if list(positions) not in pt:
        tr += 1
        if tr % 100 == 0:
            print(tr)
        legals = []
        queens = [Queen(position) for position in positions]
        for q in queens:
            legals.extend(q.moves())

        if len(set(positions).intersection(set(legals))) == 0:
            truce = True
        pt.append(list(positions))

print(positions)
