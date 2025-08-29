---
comments: True
---

# Multidimensional DP

## Table of Contents

- [ ] [120. Triangle](https://leetcode.cn/problems/triangle/) (Medium)
- [x] [64. Minimum Path Sum](https://leetcode.cn/problems/minimum-path-sum/) (Medium)
- [x] [63. Unique Paths II](https://leetcode.cn/problems/unique-paths-ii/) (Medium)
- [x] [5. Longest Palindromic Substring](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)
- [x] [97. Interleaving String](https://leetcode.cn/problems/interleaving-string/) (Medium)
- [x] [72. Edit Distance](https://leetcode.cn/problems/edit-distance/) (Medium)
- [x] [123. Best Time to Buy and Sell Stock III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) (Hard)
- [x] [188. Best Time to Buy and Sell Stock IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) (Hard)
- [ ] [221. Maximal Square](https://leetcode.cn/problems/maximal-square/) (Medium)

## 120. Triangle

-   [LeetCode](https://leetcode.com/problems/triangle/) | [LeetCode CH](https://leetcode.cn/problems/triangle/) (Medium)

-   Tags: array, dynamic programming
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

## 5. Longest Palindromic Substring

-   [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)

-   Tags: two pointers, string, dynamic programming
-   Return the longest palindromic substring in `s`.

```python title="5. Longest Palindromic Substring - Python Solution"
# DP - Interval
def longestPalindromeDP(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    start, maxLen = 0, 1

    # Init
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j]:
                if j - i <= 2:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start = i

    return s[start : start + maxLen]


# Expand Around Center
def longestPalindromeCenter(s: str) -> str:
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if len(s) <= 1:
        return s

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand_around_center(i, i)  # odd
        len2 = expand_around_center(i, i + 1)  # even

        maxLen = max(len1, len2)
        if maxLen > end - start:
            start = i - (maxLen - 1) // 2
            end = i + maxLen // 2

    return s[start : end + 1]


s = "babad"
print(longestPalindromeDP(s))  # "bab"
print(longestPalindromeCenter(s))  # "aba"

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

## 123. Best Time to Buy and Sell Stock III

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) (Hard)

-   Tags: array, dynamic programming
```python title="123. Best Time to Buy and Sell Stock III - Python Solution"
from typing import List


# 1. DP
def maxProfitDP1(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * 5 for _ in range(n)]

    dp[0][0] = 0  # no transaction
    dp[0][1] = -prices[0]  # buy 1
    dp[0][2] = 0  # sell 1
    dp[0][3] = -prices[0]  # buy 2
    dp[0][4] = 0  # sell 2

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = max(dp[i - 1][1], -prices[i])
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
        dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

    return dp[-1][4]


# 2. DP - Optimized
def maxProfitDP2(prices: List[int]) -> int:
    b1, b2 = float("inf"), float("inf")
    s1, s2 = 0, 0

    for price in prices:
        b1 = min(b1, price)
        s1 = max(s1, price - b1)
        b2 = min(b2, price - s1)
        s2 = max(s2, price - b2)

    return s2


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfitDP1(prices))  # 6
print(maxProfitDP2(prices))  # 6

```

## 188. Best Time to Buy and Sell Stock IV

-   [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | [LeetCode CH](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) (Hard)

-   Tags: array, dynamic programming
```python title="188. Best Time to Buy and Sell Stock IV - Python Solution"
from typing import List


# DP
def maxProfit(k: int, prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    dp = [[0] * (2 * k + 1) for _ in range(n)]

    for j in range(1, 2 * k, 2):
        dp[0][j] = -prices[0]

    for i in range(1, n):
        for j in range(0, 2 * k - 1, 2):
            dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
            dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])

    return dp[-1][2 * k]


k = 2
prices = [2, 4, 1]
print(maxProfit(k, prices))  # 2

```

## 221. Maximal Square

-   [LeetCode](https://leetcode.com/problems/maximal-square/) | [LeetCode CH](https://leetcode.cn/problems/maximal-square/) (Medium)

-   Tags: array, dynamic programming, matrix
