"""
-   Return the `rowIndex`th row of Pascal's triangle.
"""

from typing import List


def getRow(rowIndex: int) -> List[int]:
    dp = [[1] * (i + 1) for i in range(rowIndex + 1)]

    if rowIndex <= 1:
        return dp[rowIndex]

    for i in range(2, rowIndex + 1):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[-1]


print(getRow(rowIndex=3))  # [1, 3, 3, 1]
