---
comments: True
---

# KMP

## Table of Contents

- [x] [28. Find the Index of the First Occurrence in a String](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) (Easy)
- [x] [459. Repeated Substring Pattern](https://leetcode.cn/problems/repeated-substring-pattern/) (Easy)
- [x] [686. Repeated String Match](https://leetcode.cn/problems/repeated-string-match/) (Medium)
- [x] [1392. Longest Happy Prefix](https://leetcode.cn/problems/longest-happy-prefix/) (Hard)
- [x] [214. Shortest Palindrome](https://leetcode.cn/problems/shortest-palindrome/) (Hard)

## 28. Find the Index of the First Occurrence in a String

-   [LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [LeetCode CH](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) (Easy)

-   Tags: two pointers, string, string matching
```python title="28. Find the Index of the First Occurrence in a String - Python Solution"
from template import LPS


# Brute Force
def strStrBF(haystack: str, needle: str) -> int:
    m, n = len(haystack), len(needle)
    for i in range(m - n + 1):
        if haystack[i : i + n] == needle:
            return i
    return -1


# KMP
def strStrKMP(haystack: str, needle: str) -> int:
    lps = LPS(needle)
    m, n = len(haystack), len(needle)
    j = 0

    for i in range(m):
        while j > 0 and haystack[i] != needle[j]:
            j = lps[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == n:
            return i - n + 1
    return -1


# |------------|------------------|---------|
# |  Approach  |       Time       |  Space  |
# |------------|------------------|---------|
# | Brute Force| O((m - n) * n)   | O(1)    |
# | KMP        | O(m + n)         | O(n)    |
# |------------|------------------|---------|


haystack = "hello"
needle = "ll"
print(strStrBF(haystack, needle))  # 2
print(strStrKMP(haystack, needle))  # 2

```

## 459. Repeated Substring Pattern

-   [LeetCode](https://leetcode.com/problems/repeated-substring-pattern/) | [LeetCode CH](https://leetcode.cn/problems/repeated-substring-pattern/) (Easy)

-   Tags: string, string matching
```python title="459. Repeated Substring Pattern - Python Solution"
from template import LPS


# KMP
def repeatedSubstringPattern(s: str) -> bool:
    lps = LPS(s)
    length = len(s)

    if lps[-1] != 0 and length % (length - lps[-1]) == 0:
        return True

    return False


s = "abab"
print(repeatedSubstringPattern(s))  # True

```

## 686. Repeated String Match

-   [LeetCode](https://leetcode.com/problems/repeated-string-match/) | [LeetCode CH](https://leetcode.cn/problems/repeated-string-match/) (Medium)

-   Tags: string, string matching
```python title="686. Repeated String Match - Python Solution"
import math

from template import LPS


# KMP
def repeatedStringMatch(a: str, b: str) -> int:
    min_repeat = math.ceil(len(b) / len(a))

    def kmp(text, pattern):
        n, m = len(text), len(pattern)
        lps = LPS(pattern)
        j = 0

        for i in range(n):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]
            if text[i] == pattern[j]:
                j += 1
            if j == m:
                return i - j + 1
        return -1

    for i in range(min_repeat, min_repeat + 2):
        if kmp(a * i, b) != -1:
            return i
    return -1


print(repeatedStringMatch("abcd", "cdabcdab"))  # 3

```

## 1392. Longest Happy Prefix

-   [LeetCode](https://leetcode.com/problems/longest-happy-prefix/) | [LeetCode CH](https://leetcode.cn/problems/longest-happy-prefix/) (Hard)

-   Tags: string, rolling hash, string matching, hash function
```python title="1392. Longest Happy Prefix - Python Solution"
from template import LPS


# KMP
def longestPrefix(s: str) -> str:
    if len(s) <= 1:
        return ""

    lps = LPS(s)

    return s[: lps[-1]]


print(longestPrefix("ababab"))  # abab

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
