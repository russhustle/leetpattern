from typing import List


def getRow(rowIndex: int) -> List[int]:
    # TC: O(n^2)
    # SC: O(n^2)
    rowNum = rowIndex + 1
    dp = [[0] * i for i in range(1, rowNum + 1)]

    for i in range(rowNum):
        dp[i][0], dp[i][i] = 1, 1
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[rowIndex]


print(getRow(rowIndex=3))  # [1, 3, 3, 1]
