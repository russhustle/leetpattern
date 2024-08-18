from pprint import pprint
from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    ROWS, COLS = len(board), len(board[0])

    def capture(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
            return None

        board[r][c] = "T"
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O" and (
                r in [0, ROWS - 1] or c in [0, COLS - 1]
            ):
                capture(r, c)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "T":
                board[r][c] = "O"


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
solve(board)
pprint(board)
# [['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'O', 'X', 'X']]
