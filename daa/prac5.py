# N-Queens
def n_queens(n):
    col = set()
    # (r, c)
    posDiag = set()  # (r+c)
    negDiag = set()  # (r-c)

    # list of lists
    res = []

    # board
    board = [["0"] * n for i in range(n)]

    # backtrack
    def backtrack(r):
        # base case
        if r == n:
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return

        # recursive case
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            # place queen
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "1"

            # recurse to next row
            backtrack(r + 1)

            # backtrack to previous row
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "0"

    # backtrack to previous state
    backtrack(0)

    # print solution
    for sol in res:
        for row in sol:
            print(row)
        print()


# Driver code
if __name__ == "__main__":
    n_queens(4)
