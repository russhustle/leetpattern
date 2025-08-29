---
comments: True
---

# DP LCS Advanced

## Table of Contents

- [ ] [3290. Maximum Multiplication Score](https://leetcode.cn/problems/maximum-multiplication-score/) (Medium)
- [x] [115. Distinct Subsequences](https://leetcode.cn/problems/distinct-subsequences/) (Hard)
- [ ] [3316. Find Maximum Removals From Source String](https://leetcode.cn/problems/find-maximum-removals-from-source-string/) (Medium)
- [ ] [1639. Number of Ways to Form a Target String Given a Dictionary](https://leetcode.cn/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/) (Hard)
- [x] [97. Interleaving String](https://leetcode.cn/problems/interleaving-string/) (Medium)
- [ ] [1092. Shortest Common Supersequence ](https://leetcode.cn/problems/shortest-common-supersequence/) (Hard)
- [ ] [44. Wildcard Matching](https://leetcode.cn/problems/wildcard-matching/) (Hard)
- [ ] [10. Regular Expression Matching](https://leetcode.cn/problems/regular-expression-matching/) (Hard)

## 3290. Maximum Multiplication Score

-   [LeetCode](https://leetcode.com/problems/maximum-multiplication-score/) | [LeetCode CH](https://leetcode.cn/problems/maximum-multiplication-score/) (Medium)

-   Tags: array, dynamic programming
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

## 3316. Find Maximum Removals From Source String

-   [LeetCode](https://leetcode.com/problems/find-maximum-removals-from-source-string/) | [LeetCode CH](https://leetcode.cn/problems/find-maximum-removals-from-source-string/) (Medium)

-   Tags: array, hash table, two pointers, string, dynamic programming
## 1639. Number of Ways to Form a Target String Given a Dictionary

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/) (Hard)

-   Tags: array, string, dynamic programming
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

## 1092. Shortest Common Supersequence

-   [LeetCode](https://leetcode.com/problems/shortest-common-supersequence/) | [LeetCode CH](https://leetcode.cn/problems/shortest-common-supersequence/) (Hard)

-   Tags: string, dynamic programming
## 44. Wildcard Matching

-   [LeetCode](https://leetcode.com/problems/wildcard-matching/) | [LeetCode CH](https://leetcode.cn/problems/wildcard-matching/) (Hard)

-   Tags: string, dynamic programming, greedy, recursion
## 10. Regular Expression Matching

-   [LeetCode](https://leetcode.com/problems/regular-expression-matching/) | [LeetCode CH](https://leetcode.cn/problems/regular-expression-matching/) (Hard)

-   Tags: string, dynamic programming, recursion
