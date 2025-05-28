---
comments: True
---

# DP Grid Basics

## Table of Contents

- [x] [64. Minimum Path Sum](https://leetcode.cn/problems/minimum-path-sum/) (Medium)
- [x] [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) (Medium)
- [x] [63. Unique Paths II](https://leetcode.cn/problems/unique-paths-ii/) (Medium)
- [ ] [120. Triangle](https://leetcode.cn/problems/triangle/) (Medium)
- [ ] [3393. Count Paths With the Given XOR Value](https://leetcode.cn/problems/count-paths-with-the-given-xor-value/) (Medium)
- [ ] [931. Minimum Falling Path Sum](https://leetcode.cn/problems/minimum-falling-path-sum/) (Medium)
- [x] [2684. Maximum Number of Moves in a Grid](https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/) (Medium)
- [ ] [2304. Minimum Path Cost in a Grid](https://leetcode.cn/problems/minimum-path-cost-in-a-grid/) (Medium)
- [ ] [1289. Minimum Falling Path Sum II](https://leetcode.cn/problems/minimum-falling-path-sum-ii/) (Hard)
- [ ] [3418. Maximum Amount of Money Robot Can Earn](https://leetcode.cn/problems/maximum-amount-of-money-robot-can-earn/) (Medium)

## 64. Minimum Path Sum

-   [LeetCode](https://leetcode.com/problems/minimum-path-sum/) | [LeetCode CH](https://leetcode.cn/problems/minimum-path-sum/) (Medium)

-   Tags: array, dynamic programming, matrix

```python title="64. Minimum Path Sum - Python Solution"
from typing import List


# DP
def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i - 1][0]
    for j in range(1, n):
        dp[0][j] = grid[0][j] + dp[0][j - 1]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(grid))  # 7

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

## 120. Triangle

-   [LeetCode](https://leetcode.com/problems/triangle/) | [LeetCode CH](https://leetcode.cn/problems/triangle/) (Medium)

-   Tags: array, dynamic programming
## 3393. Count Paths With the Given XOR Value

-   [LeetCode](https://leetcode.com/problems/count-paths-with-the-given-xor-value/) | [LeetCode CH](https://leetcode.cn/problems/count-paths-with-the-given-xor-value/) (Medium)

-   Tags: array, dynamic programming, bit manipulation, matrix
## 931. Minimum Falling Path Sum

-   [LeetCode](https://leetcode.com/problems/minimum-falling-path-sum/) | [LeetCode CH](https://leetcode.cn/problems/minimum-falling-path-sum/) (Medium)

-   Tags: array, dynamic programming, matrix
## 2684. Maximum Number of Moves in a Grid

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/) (Medium)

-   Tags: array, dynamic programming, matrix

```python title="2684. Maximum Number of Moves in a Grid - Python Solution"
from typing import List


# DFS
def maxMovesDFS(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    res = 0

    def dfs(r, c):
        nonlocal res
        res = max(res, c)
        if res == n - 1:
            return

        for k in r - 1, r, r + 1:
            if 0 <= k < m and grid[k][c + 1] > grid[r][c]:
                dfs(k, c + 1)
        grid[r][c] = 0

    for i in range(m):
        dfs(i, 0)

    return res


grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
print(maxMovesDFS(grid))  # 3

```

## 2304. Minimum Path Cost in a Grid

-   [LeetCode](https://leetcode.com/problems/minimum-path-cost-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/minimum-path-cost-in-a-grid/) (Medium)

-   Tags: array, dynamic programming, matrix
## 1289. Minimum Falling Path Sum II

-   [LeetCode](https://leetcode.com/problems/minimum-falling-path-sum-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-falling-path-sum-ii/) (Hard)

-   Tags: array, dynamic programming, matrix
## 3418. Maximum Amount of Money Robot Can Earn

-   [LeetCode](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/) | [LeetCode CH](https://leetcode.cn/problems/maximum-amount-of-money-robot-can-earn/) (Medium)

-   Tags: array, dynamic programming, matrix
