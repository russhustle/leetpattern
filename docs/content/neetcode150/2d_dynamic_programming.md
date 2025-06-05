---
comments: True
---

# 2D Dynamic_Programming

## Table of Contents

- [x] [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) (Medium)
- [x] [1143. Longest Common Subsequence](https://leetcode.cn/problems/longest-common-subsequence/) (Medium)
- [x] [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) (Medium)
- [x] [518. Coin Change II](https://leetcode.cn/problems/coin-change-ii/) (Medium)
- [x] [494. Target Sum](https://leetcode.cn/problems/target-sum/) (Medium)
- [x] [97. Interleaving String](https://leetcode.cn/problems/interleaving-string/) (Medium)
- [x] [329. Longest Increasing Path in a Matrix](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) (Hard)
- [x] [115. Distinct Subsequences](https://leetcode.cn/problems/distinct-subsequences/) (Hard)
- [x] [72. Edit Distance](https://leetcode.cn/problems/edit-distance/) (Medium)
- [ ] [312. Burst Balloons](https://leetcode.cn/problems/burst-balloons/) (Hard)
- [ ] [10. Regular Expression Matching](https://leetcode.cn/problems/regular-expression-matching/) (Hard)

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

## 1143. Longest Common Subsequence

-   [LeetCode](https://leetcode.com/problems/longest-common-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-common-subsequence/) (Medium)

-   Tags: string, dynamic programming

```python title="1143. Longest Common Subsequence - Python Solution"
from functools import cache


# DP - LCS
def longestCommonSubsequenceMemo(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0
        if text1[i] == text2[j]:
            return dfs(i - 1, j - 1) + 1
        return max(dfs(i - 1, j), dfs(i, j - 1))

    return dfs(m - 1, n - 1)


# DP - LCS
def longestCommonSubsequenceTable(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


if __name__ == "__main__":
    assert longestCommonSubsequenceMemo("abcde", "ace") == 3
    assert longestCommonSubsequenceTable("abcde", "ace") == 3
    assert longestCommonSubsequenceMemo("abc", "abc") == 3
    assert longestCommonSubsequenceTable("abc", "abc") == 3

```

## 309. Best Time to Buy and Sell Stock with Cooldown

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) (Medium)

-   Tags: array, dynamic programming

```python title="309. Best Time to Buy and Sell Stock with Cooldown - Python Solution"
from typing import List


# DP
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 4 for _ in range(n)]

    dp[0][0] = -prices[0]  # poessess
    dp[0][1] = 0  # stay sold
    dp[0][2] = 0  # sell
    dp[0][3] = 0  # cooldown

    for i in range(1, n):
        dp[i][0] = max(
            dp[i - 1][0],  # stay poessess
            dp[i - 1][1] - prices[i],  # buy after stay sold
            dp[i - 1][3] - prices[i],  # buy after cooldown
        )
        dp[i][1] = max(
            dp[i - 1][1],  # stay sold
            dp[i - 1][3],  # stay cooldown
        )
        dp[i][2] = dp[i - 1][0] + prices[i]
        dp[i][3] = dp[i - 1][2]

    return max(dp[-1])


prices = [1, 2, 3, 0, 2]
print(maxProfit(prices))  # 3

```

## 518. Coin Change II

-   [LeetCode](https://leetcode.com/problems/coin-change-ii/) | [LeetCode CH](https://leetcode.cn/problems/coin-change-ii/) (Medium)

-   Tags: array, dynamic programming

```python title="518. Coin Change II - Python Solution"
from typing import List


def change(amount: int, coins: List[int]) -> int:
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], amount + 1):
            dp[j] += dp[j - coins[i]]

    return dp[-1]


amount = 5
coins = [1, 2, 5]
print(change(amount, coins))  # 4

```

## 494. Target Sum

-   [LeetCode](https://leetcode.com/problems/target-sum/) | [LeetCode CH](https://leetcode.cn/problems/target-sum/) (Medium)

-   Tags: array, dynamic programming, backtracking

```python title="494. Target Sum - Python Solution"
from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:

    totalSum = sum(nums)

    if abs(target) > totalSum:
        return 0
    if (target + totalSum) % 2 == 1:
        return 0

    targetSum = (target + totalSum) // 2
    dp = [0] * (targetSum + 1)
    dp[0] = 1

    for i in range(len(nums)):
        for j in range(targetSum, nums[i] - 1, -1):
            dp[j] += dp[j - nums[i]]

    return dp[targetSum]


nums = [1, 1, 1, 1, 1]
target = 3
print(findTargetSumWays(nums, target))  # 5

```

## 97. Interleaving String

-   [LeetCode](https://leetcode.com/problems/interleaving-string/) | [LeetCode CH](https://leetcode.cn/problems/interleaving-string/) (Medium)

-   Tags: string, dynamic programming

```python title="97. Interleaving String - Python Solution"
# DP - 2D
def isInterleaveDP(s1: str, s2: str, s3: str) -> bool:
    m, n, k = len(s1), len(s2), len(s3)

    if m + n != k:
        return False

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            )

    return dp[m][n]


# DFS
def isInterleaveDFS(s1: str, s2: str, s3: str) -> bool:
    memo = {}

    def dfs(i, j, k):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True

        if (i, j) in memo:
            return memo[(i, j)]

        res = False

        if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
            res |= dfs(i + 1, j, k + 1)

        if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
            res |= dfs(i, j + 1, k + 1)

        memo[(i, j)] = res

        return res

    return dfs(0, 0, 0)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(isInterleaveDP(s1, s2, s3))  # False
print(isInterleaveDFS(s1, s2, s3))  # False

```

## 329. Longest Increasing Path in a Matrix

-   [LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [LeetCode CH](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/) (Hard)

-   Tags: array, dynamic programming, depth first search, breadth first search, graph, topological sort, memoization, matrix

```python title="329. Longest Increasing Path in a Matrix - Python Solution"
from collections import deque
from typing import List
from functools import cache


# BFS - Topological Sort
def longestIncreasingPathBFS(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Calculate indegrees and initialize queue in one pass
    indegree = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[i][j]:
                    indegree[nr][nc] += 1

    # Start with cells that have no smaller neighbors
    queue = deque((i, j) for i in range(m) for j in range(n) if indegree[i][j] == 0)

    res = 0
    while queue:
        res += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    indegree[nr][nc] -= 1
                    if indegree[nr][nc] == 0:
                        queue.append((nr, nc))

    return res


# DP - 2D
def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    @cache
    def dfs(r, c):
        path = 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                path = max(path, dfs(nr, nc) + 1)
        return path

    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))

    return res


if __name__ == "__main__":
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    assert longestIncreasingPath(matrix) == 4
    assert longestIncreasingPathBFS(matrix) == 4

```

## 115. Distinct Subsequences

-   [LeetCode](https://leetcode.com/problems/distinct-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/distinct-subsequences/) (Hard)

-   Tags: string, dynamic programming

```python title="115. Distinct Subsequences - Python Solution"
def numDistinct(s: str, t: str) -> int:
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for _ in range((m + 1))]

    for i in range(m):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                # include and exclude s[i-1]
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]  # exclude s[i-1]

    return dp[-1][-1]


s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))  # 3

```

## 72. Edit Distance

-   [LeetCode](https://leetcode.com/problems/edit-distance/) | [LeetCode CH](https://leetcode.cn/problems/edit-distance/) (Medium)

-   Tags: string, dynamic programming

```python title="72. Edit Distance - Python Solution"
from functools import cache


# Recursive
def minDistanceDFS(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)

    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if word1[i] == word2[j]:
            return dfs(i - 1, j - 1)

        return 1 + min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1))

    return dfs(n - 1, m - 1)


# Iterative
def minDistanceDP(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no operation
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # delete
                    dp[i][j - 1],  # insert
                    dp[i - 1][j - 1],  # replace
                )
    return dp[-1][-1]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(minDistanceDFS(word1, word2))  # 3
    print(minDistanceDP(word1, word2))  # 3

```

## 312. Burst Balloons

-   [LeetCode](https://leetcode.com/problems/burst-balloons/) | [LeetCode CH](https://leetcode.cn/problems/burst-balloons/) (Hard)

-   Tags: array, dynamic programming
## 10. Regular Expression Matching

-   [LeetCode](https://leetcode.com/problems/regular-expression-matching/) | [LeetCode CH](https://leetcode.cn/problems/regular-expression-matching/) (Hard)

-   Tags: string, dynamic programming, recursion
