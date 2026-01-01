from typing import List


class gameOfLife:
    @staticmethod
    def matrix(board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        0: dead
        1: alive
        2: 10: dead -> alive
        3: 11: alive -> alive
        """
        dirs = [[0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0]]
        m, n = len(board), len(board[0])

        def count_live(r, c):
            res = 0
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] & 1:
                    res += 1
            return res

        for i in range(m):
            for j in range(n):
                cnt = count_live(i, j)
                if board[i][j] == 1:  # currently alive
                    if 2 <= cnt <= 3:
                        board[i][j] = 3  # 11: was alive, stays alive
                else:  # currently dead
                    if cnt == 3:
                        board[i][j] = 2  # 10: was dead, becomes alive

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
