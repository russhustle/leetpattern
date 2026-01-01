from copy import deepcopy
from typing import List


class setZeroes:
    @staticmethod
    def matrix(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # prep
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        # collect rows and cols
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # work on rows and cols
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        for i in range(m):
            for j in cols:
                matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes.matrix(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
