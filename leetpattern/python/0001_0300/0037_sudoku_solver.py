"""
- [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
- [解数独](https://leetcode.cn/problems/sudoku-solver/)
- Hard
"""

from pprint import pprint
from typing import List


# Backtracking - Board
def solveSudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    def backtracking(board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    continue
                for k in range(1, 10):
                    if is_valid(i, j, k, board):
                        board[i][j] = str(k)
                        if backtracking(board):
                            return True
                        board[i][j] = "."
                return False
        return True

    def is_valid(row: int, col: int, val: int, board: List[List[str]]) -> bool:
        for i in range(9):
            if board[row][i] == str(val):
                return False
        for j in range(9):
            if board[j][col] == str(val):
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(val):
                    return False
        return True

    backtracking(board)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

solveSudoku(board)
pprint(board)
# [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
#  ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
#  ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
#  ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
#  ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
#  ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
#  ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
#  ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
#  ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
