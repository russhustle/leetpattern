---
comments: True
---

# DP Optimal Partitioning

## Table of Contents

- [x] [132. Palindrome Partitioning II](https://leetcode.cn/problems/palindrome-partitioning-ii/) (Hard)
- [ ] [2707. Extra Characters in a String](https://leetcode.cn/problems/extra-characters-in-a-string/) (Medium)
- [ ] [3196. Maximize Total Cost of Alternating Subarrays](https://leetcode.cn/problems/maximize-total-cost-of-alternating-subarrays/) (Medium)
- [ ] [2767. Partition String Into Minimum Beautiful Substrings](https://leetcode.cn/problems/partition-string-into-minimum-beautiful-substrings/) (Medium)
- [x] [91. Decode Ways](https://leetcode.cn/problems/decode-ways/) (Medium)
- [ ] [639. Decode Ways II](https://leetcode.cn/problems/decode-ways-ii/) (Hard)
- [ ] [1043. Partition Array for Maximum Sum](https://leetcode.cn/problems/partition-array-for-maximum-sum/) (Medium)
- [ ] [1416. Restore The Array](https://leetcode.cn/problems/restore-the-array/) (Hard)
- [ ] [2472. Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/) (Hard)
- [ ] [1105. Filling Bookcase Shelves](https://leetcode.cn/problems/filling-bookcase-shelves/) (Medium)
- [ ] [2547. Minimum Cost to Split an Array](https://leetcode.cn/problems/minimum-cost-to-split-an-array/) (Hard)
- [ ] [2430. Maximum Deletions on a String](https://leetcode.cn/problems/maximum-deletions-on-a-string/) (Hard)
- [ ] [2463. Minimum Total Distance Traveled](https://leetcode.cn/problems/minimum-total-distance-traveled/) (Hard)
- [ ] [2977. Minimum Cost to Convert String II](https://leetcode.cn/problems/minimum-cost-to-convert-string-ii/) (Hard)
- [ ] [3441. Minimum Cost Good Caption](https://leetcode.cn/problems/minimum-cost-good-caption/) (Hard)
- [ ] [2052. Minimum Cost to Separate Sentence Into Rows](https://leetcode.cn/problems/minimum-cost-to-separate-sentence-into-rows/) (Medium) 👑
- [ ] [2464. Minimum Subarrays in a Valid Split](https://leetcode.cn/problems/minimum-subarrays-in-a-valid-split/) (Medium) 👑

## 132. Palindrome Partitioning II

-   [LeetCode](https://leetcode.com/problems/palindrome-partitioning-ii/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-partitioning-ii/) (Hard)

-   Tags: string, dynamic programming
- [教你一步步思考 DP：从记忆化搜索到递推（Python/Java/C++/Go）](https://leetcode.cn/problems/palindrome-partitioning-ii/solutions/3588633/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-bnlb)

```python title="132. Palindrome Partitioning II - Python Solution"
from functools import cache


# Memoization
def minCutMemoization(s: str) -> int:
    @cache
    def is_palindrome(left, right):
        if left >= right:
            return True
        return s[left] == s[right] and is_palindrome(left + 1, right - 1)

    @cache
    def dfs(right):
        if is_palindrome(0, right):
            return 0
        res = float("inf")
        for left in range(1, right + 1):
            if is_palindrome(left, right):
                res = min(res, 1 + dfs(left - 1))
        return res

    return dfs(len(s) - 1)


# Tabulation
def minCutTabulation(s: str) -> int:
    n = len(s)
    is_palindrome = [[True] * n for _ in range(n)]

    for left in range(n - 2, -1, -1):
        for right in range(left + 1, n):
            is_palindrome[left][right] = (
                s[left] == s[right] and is_palindrome[left + 1][right - 1]
            )

    dp = [0 for _ in range(n)]

    for right, is_pal in enumerate(is_palindrome[0]):
        if is_pal:
            continue
        res = float("inf")
        for left in range(1, right + 1):
            if is_palindrome[left][right]:
                res = min(res, 1 + dp[left - 1])
        dp[right] = res

    return dp[-1]


s = "aab"
print(minCutMemoization(s))  # 1
print(minCutTabulation(s))  # 1

```

## 2707. Extra Characters in a String

-   [LeetCode](https://leetcode.com/problems/extra-characters-in-a-string/) | [LeetCode CH](https://leetcode.cn/problems/extra-characters-in-a-string/) (Medium)

-   Tags: array, hash table, string, dynamic programming, trie

## 3196. Maximize Total Cost of Alternating Subarrays

-   [LeetCode](https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/maximize-total-cost-of-alternating-subarrays/) (Medium)

-   Tags: array, dynamic programming

## 2767. Partition String Into Minimum Beautiful Substrings

-   [LeetCode](https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/) | [LeetCode CH](https://leetcode.cn/problems/partition-string-into-minimum-beautiful-substrings/) (Medium)

-   Tags: hash table, string, dynamic programming, backtracking

## 91. Decode Ways

-   [LeetCode](https://leetcode.com/problems/decode-ways/) | [LeetCode CH](https://leetcode.cn/problems/decode-ways/) (Medium)

-   Tags: string, dynamic programming

```python title="91. Decode Ways - Python Solution"
# DP
def numDecodingsDP(s: str) -> int:
    if not s or s[0] == "0":
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        # Check single digit decode
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]

        # Check two digit decode
        if i > 1 and "10" <= s[i - 2 : i] <= "26":
            dp[i] += dp[i - 2]

    return dp[n]


# DFS
def numDecodingsDFS(s: str) -> int:
    memo = {}

    def dfs(i):
        if i == len(s):
            return 1

        if s[i] == "0":
            return 0

        if i in memo:
            return memo[i]

        # Single digit decode
        ways = dfs(i + 1)

        # Two digits decode
        if i + 1 < len(s) and "10" <= s[i : i + 2] <= "26":
            ways += dfs(i + 2)

        memo[i] = ways

        return ways

    return dfs(0)


s = "226"
print(numDecodingsDP(s))  # 3
print(numDecodingsDFS(s))  # 3

```

## 639. Decode Ways II

-   [LeetCode](https://leetcode.com/problems/decode-ways-ii/) | [LeetCode CH](https://leetcode.cn/problems/decode-ways-ii/) (Hard)

-   Tags: string, dynamic programming

## 1043. Partition Array for Maximum Sum

-   [LeetCode](https://leetcode.com/problems/partition-array-for-maximum-sum/) | [LeetCode CH](https://leetcode.cn/problems/partition-array-for-maximum-sum/) (Medium)

-   Tags: array, dynamic programming

## 1416. Restore The Array

-   [LeetCode](https://leetcode.com/problems/restore-the-array/) | [LeetCode CH](https://leetcode.cn/problems/restore-the-array/) (Hard)

-   Tags: string, dynamic programming

## 2472. Maximum Number of Non-overlapping Palindrome Substrings

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/) (Hard)

-   Tags: two pointers, string, dynamic programming, greedy

## 1105. Filling Bookcase Shelves

-   [LeetCode](https://leetcode.com/problems/filling-bookcase-shelves/) | [LeetCode CH](https://leetcode.cn/problems/filling-bookcase-shelves/) (Medium)

-   Tags: array, dynamic programming

## 2547. Minimum Cost to Split an Array

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-split-an-array/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-split-an-array/) (Hard)

-   Tags: array, hash table, dynamic programming, counting

## 2430. Maximum Deletions on a String

-   [LeetCode](https://leetcode.com/problems/maximum-deletions-on-a-string/) | [LeetCode CH](https://leetcode.cn/problems/maximum-deletions-on-a-string/) (Hard)

-   Tags: string, dynamic programming, rolling hash, string matching, hash function

## 2463. Minimum Total Distance Traveled

-   [LeetCode](https://leetcode.com/problems/minimum-total-distance-traveled/) | [LeetCode CH](https://leetcode.cn/problems/minimum-total-distance-traveled/) (Hard)

-   Tags: array, dynamic programming, sorting

## 2977. Minimum Cost to Convert String II

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-convert-string-ii/) (Hard)

-   Tags: array, string, dynamic programming, graph, trie, shortest path

## 3441. Minimum Cost Good Caption

-   [LeetCode](https://leetcode.com/problems/minimum-cost-good-caption/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-good-caption/) (Hard)

-   Tags: string, dynamic programming

## 2052. Minimum Cost to Separate Sentence Into Rows

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-separate-sentence-into-rows/) (Medium)

-   Tags: array, dynamic programming

## 2464. Minimum Subarrays in a Valid Split

-   [LeetCode](https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/) | [LeetCode CH](https://leetcode.cn/problems/minimum-subarrays-in-a-valid-split/) (Medium)

-   Tags: array, math, dynamic programming, number theory
