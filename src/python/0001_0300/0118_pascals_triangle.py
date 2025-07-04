"""
-   Generate the first `numRows` of Pascal's triangle.

```plaintext
                 numRows    index
     1              1         0
    1 1             2         1
   1 2 1            3         2
  1 3 3 1           4         3
 1 4 6 4 1          5         4
```
"""

from typing import List


def generate(numRows: int) -> List[List[int]]:
    dp = [[1] * i for i in range(1, numRows + 1)]

    if numRows <= 2:
        return dp

    for i in range(2, numRows):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp


print(generate(numRows=5))
#     [[1],
#    [1, 1],
#   [1, 2, 1],
#  [1, 3, 3, 1],
# [1, 4, 6, 4, 1]]
