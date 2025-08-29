---
comments: True
---

# DP Interval

## Table of Contents

- [x] [516. Longest Palindromic Subsequence](https://leetcode.cn/problems/longest-palindromic-subsequence/) (Medium)
- [x] [647. Palindromic Substrings](https://leetcode.cn/problems/palindromic-substrings/) (Medium)
- [x] [5. Longest Palindromic Substring](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)

## 516. Longest Palindromic Subsequence

-   [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindromic-subsequence/) (Medium)

-   Tags: string, dynamic programming
-   Return the length of the longest palindromic subsequence in `s`.
-   Bottom-up DP table

| dp  |  b  |  b  |  b  |        a         |      b       |
| :-: | :-: | :-: | :-: | :--------------: | :----------: |
|  b  |  1  |  2  |  3  |        3         |      4       |
|  b  |  0  |  1  |  2  |        2         | 3 `dp[i][j]` |
|  b  |  0  |  0  |  1  | 1 `dp[i+1][j-1]` |      2       |
|  a  |  0  |  0  |  0  |        1         |      1       |
|  b  |  0  |  0  |  0  |        0         |      1       |

```python title="516. Longest Palindromic Subsequence - Python Solution"
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    return dp[0][-1]


print(longestPalindromeSubseq("bbbab"))  # 4

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

