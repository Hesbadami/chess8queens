import random


class Board:  # our chromosome
    def __init__(self, board=None):
        self.board = board
        if self.board is None:
            self.board = []
            for i in range(8):
                rank = [0]*7 + [1]*1  # our gene
                random.shuffle(rank)
                self.board.append(rank)

    def get_board(self):
        return self.board

    def fittness(self):
        # 64 - number of queens attacking each other
        board = self.board
        count = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    # if queen exists
                    # there are no horizental attacks
                    # Vertical towards rank 8:
                    r, f = i, j
                    while r > 0:
                        r -= 1
                        if board[r][f] == 1:
                            count += 1
                            break

                    # Vertical towards rank 1:
                    r, f = i, j
                    while r < 7:
                        r += 1
                        if board[r][f] == 1:
                            count += 1
                            break

                    # Diagonal towards upperleft
                    r, f = i, j
                    while r > 0 and f > 0:
                        r -= 1
                        f -= 1
                        if board[r][f] == 1:
                            count += 1
                            break

                    # Diagonal towards lowerleft
                    r, f = i, j
                    while r > 0 and f < 7:
                        r -= 1
                        f += 1
                        if board[r][f] == 1:
                            count += 1
                            break

                    # Diagonal towards upperright
                    r, f = i, j
                    while r < 7 and f > 0:
                        r += 1
                        f -= 1
                        if board[r][f] == 1:
                            count += 1
                            break

                    # Diagonal towards lowerright
                    r, f = i, j
                    while r < 7 and f < 7:
                        r += 1
                        f += 1
                        if board[r][f] == 1:
                            count += 1
                            break

        self.ft = 64 - count
        return 64 - count

    def mutate(self, possibility=0.000625):
        if possibility >= random.randint(0, 1000)/1000:
            rank_i = random.randint(1, 7)  # rank number to be replaced
            newrank = [0]*7 + [1]*1  # new rank
            random.shuffle(newrank)
            self.board[rank_i] = newrank

    def breed(self, mate):
        cut = random.randint(0, 7)
        child1 = Board(self.get_board()[:cut] + mate.get_board()[cut:])
        child2 = Board(self.get_board()[cut:] + mate.get_board()[:cut])
        return child1, child2
