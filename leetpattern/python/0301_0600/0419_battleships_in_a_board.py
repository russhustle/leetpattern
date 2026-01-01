from typing import List


class CountBattleships:
    def matrix(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    # 如果上面或左边有 X，就不是新的战舰
                    if i > 0 and board[i - 1][j] == "X":
                        continue
                    if j > 0 and board[i][j - 1] == "X":
                        continue
                    res += 1

        return res


if __name__ == "__main__":
    sol = CountBattleships()
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    assert sol.matrix(board) == 2
