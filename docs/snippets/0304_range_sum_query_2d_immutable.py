from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return None

        self.sum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sum[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.sum[i - 1][j]
                    + self.sum[i][j - 1]
                    - self.sum[i - 1][j - 1]  # to avoid double counting
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sum[row2 + 1][col2 + 1]
            - self.sum[row1][col2 + 1]
            - self.sum[row2 + 1][col1]
            + self.sum[row1][col1]
        )


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]
obj = NumMatrix(matrix)
assert obj.sumRegion(2, 1, 4, 3) == 8
assert obj.sumRegion(1, 1, 2, 2) == 11
assert obj.sumRegion(1, 2, 2, 4) == 12
print("PASSED")
