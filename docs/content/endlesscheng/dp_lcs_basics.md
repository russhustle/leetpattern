---
comments: True
---

# DP LCS Basics

## Table of Contents

- [x] [1143. Longest Common Subsequence](https://leetcode.cn/problems/longest-common-subsequence/) (Medium)
- [x] [583. Delete Operation for Two Strings](https://leetcode.cn/problems/delete-operation-for-two-strings/) (Medium)
- [ ] [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/) (Medium)
- [x] [72. Edit Distance](https://leetcode.cn/problems/edit-distance/) (Medium)
- [x] [1035. Uncrossed Lines](https://leetcode.cn/problems/uncrossed-lines/) (Medium)
- [ ] [1458. Max Dot Product of Two Subsequences](https://leetcode.cn/problems/max-dot-product-of-two-subsequences/) (Hard)

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

## 583. Delete Operation for Two Strings

-   [LeetCode](https://leetcode.com/problems/delete-operation-for-two-strings/) | [LeetCode CH](https://leetcode.cn/problems/delete-operation-for-two-strings/) (Medium)

-   Tags: string, dynamic programming

```python title="583. Delete Operation for Two Strings - Python Solution"
# DP - LCS
def minDistance1(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no need to delete
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # delete word1[i]
                    dp[i][j - 1] + 1,  # delete word2[j]
                    dp[i - 1][j - 1] + 2,  # delete both
                )
    return dp[-1][-1]


# DP - LCS
def minDistance2(word1: str, word2: str) -> int:
    def LCS(word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        lcs = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                if lcs < dp[i][j]:
                    lcs = dp[i][j]
        return lcs

    lcs = LCS(word1, word2)
    return len(word1) + len(word2) - 2 * lcs


word1 = "sea"
word2 = "eat"
print(minDistance1(word1, word2))  # 2
print(minDistance2(word1, word2))  # 2

```

## 712. Minimum ASCII Delete Sum for Two Strings

-   [LeetCode](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) | [LeetCode CH](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/) (Medium)

-   Tags: string, dynamic programming
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

## 1035. Uncrossed Lines

-   [LeetCode](https://leetcode.com/problems/uncrossed-lines/) | [LeetCode CH](https://leetcode.cn/problems/uncrossed-lines/) (Medium)

-   Tags: array, dynamic programming

```python title="1035. Uncrossed Lines - Python Solution"
from typing import List


def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    m = len(nums1)
    n = len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    num = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            if num < dp[i][j]:
                num = dp[i][j]

    return num


print(maxUncrossedLines([1, 4, 2], [1, 2, 4]))  # 2

```

## 1458. Max Dot Product of Two Subsequences

-   [LeetCode](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/max-dot-product-of-two-subsequences/) (Hard)

-   Tags: array, dynamic programming
