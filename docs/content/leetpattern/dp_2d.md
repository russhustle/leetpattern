---
comments: True
---

# DP 2D

## Table of Contents

- [x] [118. Pascal's Triangle](https://leetcode.cn/problems/pascals-triangle/) (Easy)
- [x] [119. Pascal's Triangle II](https://leetcode.cn/problems/pascals-triangle-ii/) (Easy)
- [x] [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) (Medium)
- [x] [63. Unique Paths II](https://leetcode.cn/problems/unique-paths-ii/) (Medium)

## 118. Pascal's Triangle

-   [LeetCode](https://leetcode.com/problems/pascals-triangle/) | [LeetCode CH](https://leetcode.cn/problems/pascals-triangle/) (Easy)

-   Tags: array, dynamic programming
-   Generate the first `numRows` of Pascal's triangle.

```plaintext
                 numRows
     1              1
    1 1             2
   1 2 1            3
  1 3 3 1           4
 1 4 6 4 1          5
```


```python title="118. Pascal's Triangle - Python Solution"
from typing import List


def generate(numRows: int) -> List[List[int]]:
    dp = [[1] * i for i in range(1, numRows + 1)]

    if numRows <= 2:
        return dp

    for i in range(2, numRows):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp


if __name__ == "__main__":
    print(generate(numRows=5))
    # [[1],
    #  [1, 1],
    #  [1, 2, 1],
    #  [1, 3, 3, 1],
    #  [1, 4, 6, 4, 1]]

```

## 119. Pascal's Triangle II

-   [LeetCode](https://leetcode.com/problems/pascals-triangle-ii/) | [LeetCode CH](https://leetcode.cn/problems/pascals-triangle-ii/) (Easy)

-   Tags: array, dynamic programming
-   Return the `rowIndex`th row of Pascal's triangle.


```python title="119. Pascal's Triangle II - Python Solution"
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

```

## 62. Unique Paths

-   [LeetCode](https://leetcode.com/problems/unique-paths/) | [LeetCode CH](https://leetcode.cn/problems/unique-paths/) (Medium)

-   Tags: math, dynamic programming, combinatorics
-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid.

![62](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)


```python title="62. Unique Paths - Python Solution"
# DP - 2D
def uniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1

    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


print(uniquePaths(m=3, n=7))  # 28
# [[1, 1, 1,  1,  1,  1,  1],
#  [1, 2, 3,  4,  5,  6,  7],
#  [1, 3, 6, 10, 15, 21, 28]]

```

```cpp title="62. Unique Paths - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

int uniquePaths(int m, int n) {
    vector dp(m, vector<int>(n, 1));

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }

    return dp[m - 1][n - 1];
}

int main() {
    int m = 3, n = 7;
    cout << uniquePaths(m, n) << endl;  // 28
    return 0;
}

```

## 63. Unique Paths II

-   [LeetCode](https://leetcode.com/problems/unique-paths-ii/) | [LeetCode CH](https://leetcode.cn/problems/unique-paths-ii/) (Medium)

-   Tags: array, dynamic programming, matrix
-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid with obstacles.

![63](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)


```python title="63. Unique Paths II - Python Solution"
from typing import List


# DP - 2D
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = 1
        else:
            break

    for j in range(n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = 1
        else:
            break

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(obstacleGrid))  # 2
# [[1, 1, 1],
#  [1, 0, 1],
#  [1, 1, 2]]

```
