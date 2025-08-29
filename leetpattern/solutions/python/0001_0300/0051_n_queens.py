"""
- Hard
- [N-Queens](https://leetcode.com/problems/n-queens/)
- [N 皇后](https://leetcode.cn/problems/n-queens/)
"""

from typing import List


# Backtracking
def solveNQueens(n: int) -> List[List[str]]:
    res = []
    board = ["." * n for _ in range(n)]

    def dfs(row):
        if row == n:
            res.append(board[:])
            return None
        for col in range(n):
            if is_valid(row, col, board):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                dfs(row + 1)
                board[row] = board[row][:col] + "." + board[row][col + 1 :]

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

    dfs(0)

    return [["".join(row) for row in i] for i in res]


# Backtracking
def solveNQueens2(n: int) -> List[List[str]]:
    res = []
    queens = [0] * n
    col = [False] * n
    diag1 = [False] * (n * 2 - 1)
    diag2 = [False] * (n * 2 - 1)

    def dfs(r: int) -> None:
        if r == n:
            res.append(["." * c + "Q" + "." * (n - 1 - c) for c in queens])
            return

        for c, ok in enumerate(col):
            if not ok and not diag1[r + c] and not diag2[r - c]:
                queens[r] = c
                col[c] = diag1[r + c] = diag2[r - c] = True
                dfs(r + 1)
                col[c] = diag1[r + c] = diag2[r - c] = False

    dfs(0)

    return res


if __name__ == "__main__":
    print(solveNQueens(4))
    # [['.Q..', '...Q', 'Q...', '..Q.'],
    #  ['..Q.', 'Q...', '...Q', '.Q..']]
    print(solveNQueens(1))
    # [['Q']]
    print(solveNQueens2(4))
    # [['.Q..', '...Q', 'Q...', '..Q.'],
    #  ['..Q.', 'Q...', '...Q', '.Q..']]
    print(solveNQueens2(1))
    # [['Q']]
