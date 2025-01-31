from typing import List


# Set
def isValidSudoku(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue

            if board[i][j] in rows[i]:
                return False
            rows[i].add(board[i][j])

            if board[i][j] in cols[j]:
                return False
            cols[j].add(board[i][j])

            box_index = (i // 3) * 3 + j // 3
            if board[i][j] in boxes[box_index]:
                return False
            boxes[box_index].add(board[i][j])

    return True


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
print(isValidSudoku(board))  # True
