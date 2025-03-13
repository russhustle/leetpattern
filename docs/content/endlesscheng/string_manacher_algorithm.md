---
comments: True
---

# String Manacher Algorithm

- [x] [5. Longest Palindromic Substring](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)
- [x] [647. Palindromic Substrings](https://leetcode.cn/problems/palindromic-substrings/) (Medium)
- [x] [214. Shortest Palindrome](https://leetcode.cn/problems/shortest-palindrome/) (Hard)
- [ ] [3327. Check if DFS Strings Are Palindromes](https://leetcode.cn/problems/check-if-dfs-strings-are-palindromes/) (Hard)
- [x] [1745. Palindrome Partitioning IV](https://leetcode.cn/problems/palindrome-partitioning-iv/) (Hard)
- [ ] [1960. Maximum Product of the Length of Two Palindromic Substrings](https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-substrings/) (Hard)

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

## 214. Shortest Palindrome

-   [LeetCode](https://leetcode.com/problems/shortest-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/shortest-palindrome/) (Hard)

-   Tags: string, rolling hash, string matching, hash function

```python title="214. Shortest Palindrome - Python Solution"
from template import LPS


# KMP
def shortestPalindrome(s: str) -> str:
    if not s:
        return s

    new = s + "#" + s[::-1]
    lps = LPS(new)

    add_len = len(s) - lps[-1]

    return s[::-1][:add_len] + s


print(shortestPalindrome("aacecaaa"))  # aaacecaaa

```

## 3327. Check if DFS Strings Are Palindromes

-   [LeetCode](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/) | [LeetCode CH](https://leetcode.cn/problems/check-if-dfs-strings-are-palindromes/) (Hard)

-   Tags: array, hash table, string, tree, depth first search, hash function

## 1745. Palindrome Partitioning IV

-   [LeetCode](https://leetcode.com/problems/palindrome-partitioning-iv/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-partitioning-iv/) (Hard)

-   Tags: string, dynamic programming

```python title="1745. Palindrome Partitioning IV - Python Solution"
# DP
def checkPartitioning(s: str) -> bool:
    def palidrome_partition(s, k):
        n = len(s)
        min_change = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                min_change[i][j] = min_change[i + 1][j - 1] + (
                    1 if s[i] != s[j] else 0
                )

        dp = min_change[0]

        for i in range(1, k):
            for right in range(n - k + i, i - 1, -1):
                dp[right] = min(
                    dp[left - 1] + min_change[left][right]
                    for left in range(i, right + 1)
                )

        return dp[-1]

    return palidrome_partition(s, 3) == 0


s = "abcbdd"
print(checkPartitioning(s))  # True

```

## 1960. Maximum Product of the Length of Two Palindromic Substrings

-   [LeetCode](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/) | [LeetCode CH](https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-substrings/) (Hard)

-   Tags: string, rolling hash, hash function
