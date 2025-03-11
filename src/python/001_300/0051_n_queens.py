from typing import List


# Backtracking - Board
def solveNQueens(n: int) -> List[List[str]]:
    result = []
    chessboard = ["." * n for _ in range(n)]

    def backtracking(row):
        if row == n:
            result.append(chessboard[:])
            return None
        for col in range(n):
            if is_valid(row, col, chessboard):
                chessboard[row] = (
                    chessboard[row][:col] + "Q" + chessboard[row][col + 1 :]
                )
                backtracking(row + 1)
                chessboard[row] = (
                    chessboard[row][:col] + "." + chessboard[row][col + 1 :]
                )

    def is_valid(row, col, chessboard):
        for i in range(row):
            if chessboard[i][col] == "Q":
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    backtracking(0)

    return [["".join(row) for row in solution] for solution in result]


print(solveNQueens(4))
# [['.Q..', '...Q', 'Q...', '..Q.'],
#  ['..Q.', 'Q...', '...Q', '.Q..']]
