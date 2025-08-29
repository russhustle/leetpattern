---
comments: True
---

# 2D Dynamic Programming

## Table of Contents

- [x] [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) (Medium)
- [x] [1143. Longest Common Subsequence](https://leetcode.cn/problems/longest-common-subsequence/) (Medium)

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

