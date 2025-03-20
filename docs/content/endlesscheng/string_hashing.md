---
comments: True
---

# String Hashing

## Table of Contents

- [x] [28. Find the Index of the First Occurrence in a String](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/) (Easy)
- [ ] [187. Repeated DNA Sequences](https://leetcode.cn/problems/repeated-dna-sequences/) (Medium)
- [ ] [1316. Distinct Echo Substrings](https://leetcode.cn/problems/distinct-echo-substrings/) (Hard)
- [ ] [1297. Maximum Number of Occurrences of a Substring](https://leetcode.cn/problems/maximum-number-of-occurrences-of-a-substring/) (Medium)
- [ ] [2261. K Divisible Elements Subarrays](https://leetcode.cn/problems/k-divisible-elements-subarrays/) (Medium)
- [ ] [3213. Construct String with Minimum Cost](https://leetcode.cn/problems/construct-string-with-minimum-cost/) (Hard)
- [ ] [1367. Linked List in Binary Tree](https://leetcode.cn/problems/linked-list-in-binary-tree/) (Medium)
- [ ] [1044. Longest Duplicate Substring](https://leetcode.cn/problems/longest-duplicate-substring/) (Hard)
- [x] [718. Maximum Length of Repeated Subarray](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) (Medium)
- [ ] [1923. Longest Common Subpath](https://leetcode.cn/problems/longest-common-subpath/) (Hard)
- [ ] [3292. Minimum Number of Valid Strings to Form Target II](https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/) (Hard)
- [ ] [2168. Unique Substrings With Equal Digit Frequency](https://leetcode.cn/problems/unique-substrings-with-equal-digit-frequency/) (Medium) 👑
- [ ] [1554. Strings Differ by One Character](https://leetcode.cn/problems/strings-differ-by-one-character/) (Medium) 👑
- [ ] [1062. Longest Repeating Substring](https://leetcode.cn/problems/longest-repeating-substring/) (Medium) 👑

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

## 187. Repeated DNA Sequences

-   [LeetCode](https://leetcode.com/problems/repeated-dna-sequences/) | [LeetCode CH](https://leetcode.cn/problems/repeated-dna-sequences/) (Medium)

-   Tags: hash table, string, bit manipulation, sliding window, rolling hash, hash function

## 1316. Distinct Echo Substrings

-   [LeetCode](https://leetcode.com/problems/distinct-echo-substrings/) | [LeetCode CH](https://leetcode.cn/problems/distinct-echo-substrings/) (Hard)

-   Tags: string, trie, rolling hash, hash function

## 1297. Maximum Number of Occurrences of a Substring

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-occurrences-of-a-substring/) (Medium)

-   Tags: hash table, string, sliding window

## 2261. K Divisible Elements Subarrays

-   [LeetCode](https://leetcode.com/problems/k-divisible-elements-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/k-divisible-elements-subarrays/) (Medium)

-   Tags: array, hash table, trie, rolling hash, hash function, enumeration

## 3213. Construct String with Minimum Cost

-   [LeetCode](https://leetcode.com/problems/construct-string-with-minimum-cost/) | [LeetCode CH](https://leetcode.cn/problems/construct-string-with-minimum-cost/) (Hard)

-   Tags: array, string, dynamic programming, suffix array

## 1367. Linked List in Binary Tree

-   [LeetCode](https://leetcode.com/problems/linked-list-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/linked-list-in-binary-tree/) (Medium)

-   Tags: linked list, tree, depth first search, binary tree

## 1044. Longest Duplicate Substring

-   [LeetCode](https://leetcode.com/problems/longest-duplicate-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-duplicate-substring/) (Hard)

-   Tags: string, binary search, sliding window, rolling hash, suffix array, hash function

## 718. Maximum Length of Repeated Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) (Medium)

-   Tags: array, binary search, dynamic programming, sliding window, rolling hash, hash function

```python title="718. Maximum Length of Repeated Subarray - Python Solution"
from typing import List


def findLength(nums1: List[int], nums2: List[int]) -> int:
    m = len(nums1)
    n = len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            if length < dp[i][j]:
                length = dp[i][j]

    return length


print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3

```

## 1923. Longest Common Subpath

-   [LeetCode](https://leetcode.com/problems/longest-common-subpath/) | [LeetCode CH](https://leetcode.cn/problems/longest-common-subpath/) (Hard)

-   Tags: array, binary search, rolling hash, suffix array, hash function

## 3292. Minimum Number of Valid Strings to Form Target II

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/) (Hard)

-   Tags: array, string, binary search, dynamic programming, segment tree, rolling hash, string matching, hash function

## 2168. Unique Substrings With Equal Digit Frequency

-   [LeetCode](https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/) | [LeetCode CH](https://leetcode.cn/problems/unique-substrings-with-equal-digit-frequency/) (Medium)

-   Tags: hash table, string, rolling hash, counting, hash function

## 1554. Strings Differ by One Character

-   [LeetCode](https://leetcode.com/problems/strings-differ-by-one-character/) | [LeetCode CH](https://leetcode.cn/problems/strings-differ-by-one-character/) (Medium)

-   Tags: hash table, string, rolling hash, hash function

## 1062. Longest Repeating Substring

-   [LeetCode](https://leetcode.com/problems/longest-repeating-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-repeating-substring/) (Medium)

-   Tags: string, binary search, dynamic programming, rolling hash, suffix array, hash function
