---
comments: True
---

# Multi-dimensional Dynamic Programming

## Table of Contents

- [x] [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) (Medium)
- [x] [64. Minimum Path Sum](https://leetcode.cn/problems/minimum-path-sum/) (Medium)
- [x] [5. Longest Palindromic Substring](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)
- [x] [1143. Longest Common Subsequence](https://leetcode.cn/problems/longest-common-subsequence/) (Medium)
- [x] [72. Edit Distance](https://leetcode.cn/problems/edit-distance/) (Medium)

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

## 1143. Longest Common Subsequence

-   [LeetCode](https://leetcode.com/problems/longest-common-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-common-subsequence/) (Medium)

-   Tags: string, dynamic programming

```python title="1143. Longest Common Subsequence - Python Solution"
# DP (LCS)
def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Computes the length of the longest common subsequence between two strings.

    dp[i][j]: the length of the LCS between text1[:i] and text2[:j].

    Args:
        text1 (str): The first string.
        text2 (str): The second string.

    Returns:
        int: The length of the longest common subsequence.

    Example:
        >>> longestCommonSubsequence("abcde", "ace")
        3
        >>> longestCommonSubsequence("abc", "abc")
        3
        >>> longestCommonSubsequence("abc", "def")
        0
    """

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
    import doctest

    doctest.testmod()

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
