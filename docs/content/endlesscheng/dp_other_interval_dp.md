---
comments: True
---

# DP Other Interval DP

## Table of Contents

- [x] [5. Longest Palindromic Substring](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)
- [x] [647. Palindromic Substrings](https://leetcode.cn/problems/palindromic-substrings/) (Medium)
- [ ] [3040. Maximum Number of Operations With the Same Score II](https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/) (Medium)
- [ ] [375. Guess Number Higher or Lower II](https://leetcode.cn/problems/guess-number-higher-or-lower-ii/) (Medium)
- [ ] [1130. Minimum Cost Tree From Leaf Values](https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/) (Medium)
- [ ] [96. Unique Binary Search Trees](https://leetcode.cn/problems/unique-binary-search-trees/) (Medium)
- [ ] [1770. Maximum Score from Performing Multiplication Operations](https://leetcode.cn/problems/maximum-score-from-performing-multiplication-operations/) (Hard)
- [ ] [1547. Minimum Cost to Cut a Stick](https://leetcode.cn/problems/minimum-cost-to-cut-a-stick/) (Hard)
- [ ] [1039. Minimum Score Triangulation of Polygon](https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/) (Medium)
- [ ] [1000. Minimum Cost to Merge Stones](https://leetcode.cn/problems/minimum-cost-to-merge-stones/) (Hard)
- [ ] [2019. The Score of Students Solving Math Expression](https://leetcode.cn/problems/the-score-of-students-solving-math-expression/) (Hard)
- [ ] [3277. Maximum XOR Score Subarray Queries](https://leetcode.cn/problems/maximum-xor-score-subarray-queries/) (Hard)
- [ ] [87. Scramble String](https://leetcode.cn/problems/scramble-string/) (Hard)
- [ ] [312. Burst Balloons](https://leetcode.cn/problems/burst-balloons/) (Hard)
- [ ] [664. Strange Printer](https://leetcode.cn/problems/strange-printer/) (Hard)
- [ ] [546. Remove Boxes](https://leetcode.cn/problems/remove-boxes/) (Hard)
- [ ] [471. Encode String with Shortest Length](https://leetcode.cn/problems/encode-string-with-shortest-length/) (Hard) 👑
- [ ] [3018. Maximum Number of Removal Queries That Can Be Processed I](https://leetcode.cn/problems/maximum-number-of-removal-queries-that-can-be-processed-i/) (Hard) 👑

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

## 647. Palindromic Substrings

-   [LeetCode](https://leetcode.com/problems/palindromic-substrings/) | [LeetCode CH](https://leetcode.cn/problems/palindromic-substrings/) (Medium)

-   Tags: two pointers, string, dynamic programming
-   Return the number of palindromic substrings in `s`.
-   Bottom-up DP table

|  dp   |  a  |  b  |  b  |  a  |  e  |
| :---: | :-: | :-: | :-: | :-: | :-: |
| **a** |  1  |  0  |  0  |  1  |  0  |
| **b** |  0  |  1  |  1  |  0  |  0  |
| **b** |  0  |  0  |  1  |  0  |  0  |
| **a** |  0  |  0  |  0  |  1  |  0  |
| **e** |  0  |  0  |  0  |  0  |  1  |

```python title="647. Palindromic Substrings - Python Solution"
def countSubstrings(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    res = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = 1
                    res += 1
                elif dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    res += 1

    return res


print(countSubstrings("abbae"))  # 7

```

## 3040. Maximum Number of Operations With the Same Score II

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/) (Medium)

-   Tags: array, dynamic programming, memoization
## 375. Guess Number Higher or Lower II

-   [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) | [LeetCode CH](https://leetcode.cn/problems/guess-number-higher-or-lower-ii/) (Medium)

-   Tags: math, dynamic programming, game theory
## 1130. Minimum Cost Tree From Leaf Values

-   [LeetCode](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/) (Medium)

-   Tags: array, dynamic programming, stack, greedy, monotonic stack
## 96. Unique Binary Search Trees

-   [LeetCode](https://leetcode.com/problems/unique-binary-search-trees/) | [LeetCode CH](https://leetcode.cn/problems/unique-binary-search-trees/) (Medium)

-   Tags: math, dynamic programming, tree, binary search tree, binary tree
## 1770. Maximum Score from Performing Multiplication Operations

-   [LeetCode](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/) | [LeetCode CH](https://leetcode.cn/problems/maximum-score-from-performing-multiplication-operations/) (Hard)

-   Tags: array, dynamic programming
## 1547. Minimum Cost to Cut a Stick

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-cut-a-stick/) (Hard)

-   Tags: array, dynamic programming, sorting
## 1039. Minimum Score Triangulation of Polygon

-   [LeetCode](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) | [LeetCode CH](https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/) (Medium)

-   Tags: array, dynamic programming
## 1000. Minimum Cost to Merge Stones

-   [LeetCode](https://leetcode.com/problems/minimum-cost-to-merge-stones/) | [LeetCode CH](https://leetcode.cn/problems/minimum-cost-to-merge-stones/) (Hard)

-   Tags: array, dynamic programming, prefix sum
## 2019. The Score of Students Solving Math Expression

-   [LeetCode](https://leetcode.com/problems/the-score-of-students-solving-math-expression/) | [LeetCode CH](https://leetcode.cn/problems/the-score-of-students-solving-math-expression/) (Hard)

-   Tags: array, math, string, dynamic programming, stack, memoization
## 3277. Maximum XOR Score Subarray Queries

-   [LeetCode](https://leetcode.com/problems/maximum-xor-score-subarray-queries/) | [LeetCode CH](https://leetcode.cn/problems/maximum-xor-score-subarray-queries/) (Hard)

-   Tags: array, dynamic programming
## 87. Scramble String

-   [LeetCode](https://leetcode.com/problems/scramble-string/) | [LeetCode CH](https://leetcode.cn/problems/scramble-string/) (Hard)

-   Tags: string, dynamic programming
## 312. Burst Balloons

-   [LeetCode](https://leetcode.com/problems/burst-balloons/) | [LeetCode CH](https://leetcode.cn/problems/burst-balloons/) (Hard)

-   Tags: array, dynamic programming
## 664. Strange Printer

-   [LeetCode](https://leetcode.com/problems/strange-printer/) | [LeetCode CH](https://leetcode.cn/problems/strange-printer/) (Hard)

-   Tags: string, dynamic programming
## 546. Remove Boxes

-   [LeetCode](https://leetcode.com/problems/remove-boxes/) | [LeetCode CH](https://leetcode.cn/problems/remove-boxes/) (Hard)

-   Tags: array, dynamic programming, memoization
## 471. Encode String with Shortest Length

-   [LeetCode](https://leetcode.com/problems/encode-string-with-shortest-length/) | [LeetCode CH](https://leetcode.cn/problems/encode-string-with-shortest-length/) (Hard)

-   Tags: string, dynamic programming
## 3018. Maximum Number of Removal Queries That Can Be Processed I

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-removal-queries-that-can-be-processed-i/) (Hard)

-   Tags: array, dynamic programming
