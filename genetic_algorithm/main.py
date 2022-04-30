from time import time
from copy import deepcopy
from Evolution import Genetics


def printboard(Board):
    board = deepcopy(Board)
    qq = "♕"
    sqb = "◼"
    sqw = "◻"
    white = False
    for r in range(8):
        if white:
            white = False
        else:
            white = True
        for f in range(8):
            if board[r][f] == 1:
                board[r][f] = qq
                if white:
                    white = False
                else:
                    white = True
            else:
                if white:
                    board[r][f] = sqw
                    white = False
                else:
                    board[r][f] = sqb
                    white = True

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


population = 2000
max_iter = 800
pb = 0.80
pm = 0.5
max_fittness = 64

a = time()
x = Genetics(
    population=population,  # population
    max_iter=max_iter,  # max number of generations
    pb=pb,  # breeding probability
    pm=pm,  # mutation probability
    max_fittness=max_fittness
)

print("Gen", "\tBest", "\tAvg")

while not x.terminate():
    print(
        x.generation, "\t"+str(x.best_fittness[-1]),
        "\t"+str(x.avg_fittness[-1])
    )
    x.next_gen()

b = time()
print("Time:", round(b-a, 2), "seconds")
printboard(x.final_ans.get_board())
