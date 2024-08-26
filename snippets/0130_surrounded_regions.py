from collections import deque
from copy import deepcopy
from pprint import pprint
from typing import List


# 1. DFS
def solveDFS(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board and not board[0]:
        return None

    m, n = len(board), len(board[0])

    def capture(r, c):
        if r not in range(m) or c not in range(n) or board[r][c] != "O":
            return None

        board[r][c] = "T"
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    for r in range(m):
        for c in range(n):
            if board[r][c] == "O" and (r in [0, m - 1] or c in [0, n - 1]):
                capture(r, c)

    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"

    for r in range(m):
        for c in range(n):
            if board[r][c] == "T":
                board[r][c] = "O"


# 2. BFS
def solveBFS(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board and not board[0]:
        return None

    m, n = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def capture(r, c):
        q = deque([(r, c)])

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if nr in range(m) and nc in range(n) and board[nr][nc] == "O":
                    q.append((nr, nc))
                    board[nr][nc] = "T"

    for r in range(m):
        for c in range(n):
            if board[r][c] == "O" and (r in [0, m - 1] or c in [0, n - 1]):
                board[r][c] = "T"
                capture(r, c)

    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"

    for r in range(m):
        for c in range(n):
            if board[r][c] == "T":
                board[r][c] = "O"


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
board1 = deepcopy(board)
solveDFS(board1)
pprint(board1)
# [['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'O', 'X', 'X']]

board2 = deepcopy(board)
solveBFS(board2)
pprint(board2)
# [['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'X', 'X', 'X'],
#  ['X', 'O', 'X', 'X']]
