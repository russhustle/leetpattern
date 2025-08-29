---
comments: True
---

# Two Sequences Subsequence Checking

## Table of Contents

- [x] [392. Is Subsequence](https://leetcode.cn/problems/is-subsequence/) (Easy)
- [ ] [524. Longest Word in Dictionary through Deleting](https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/) (Medium)
- [ ] [2486. Append Characters to String to Make Subsequence](https://leetcode.cn/problems/append-characters-to-string-to-make-subsequence/) (Medium)
- [ ] [2825. Make String a Subsequence Using Cyclic Increments](https://leetcode.cn/problems/make-string-a-subsequence-using-cyclic-increments/) (Medium)
- [ ] [1023. Camelcase Matching](https://leetcode.cn/problems/camelcase-matching/) (Medium)
- [ ] [3132. Find the Integer Added to Array II](https://leetcode.cn/problems/find-the-integer-added-to-array-ii/) (Medium)
- [ ] [522. Longest Uncommon Subsequence II](https://leetcode.cn/problems/longest-uncommon-subsequence-ii/) (Medium)
- [ ] [1898. Maximum Number of Removable Characters](https://leetcode.cn/problems/maximum-number-of-removable-characters/) (Medium)
- [ ] [2565. Subsequence With the Minimum Score](https://leetcode.cn/problems/subsequence-with-the-minimum-score/) (Hard)
- [ ] [3302. Find the Lexicographically Smallest Valid Sequence](https://leetcode.cn/problems/find-the-lexicographically-smallest-valid-sequence/) (Medium)

## 392. Is Subsequence

-   [LeetCode](https://leetcode.com/problems/is-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/is-subsequence/) (Easy)

-   Tags: two pointers, string, dynamic programming
```python title="392. Is Subsequence - Python Solution"
# DP - LCS
def isSubsequenceLCS(s: str, t: str) -> bool:
    m = len(s)
    n = len(t)

    if m > n:
        return False

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]  # only delete t string

            if length < dp[i][j]:
                length = dp[i][j]

    return length == m


# Two Pointers
def isSubsequenceTP(s: str, t: str) -> bool:
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


s = "abc"
t = "ahbgdc"
print(isSubsequenceLCS(s, t))  # True
print(isSubsequenceTP(s, t))  # True

```

## 524. Longest Word in Dictionary through Deleting

-   [LeetCode](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) | [LeetCode CH](https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/) (Medium)

-   Tags: array, two pointers, string, sorting
## 2486. Append Characters to String to Make Subsequence

-   [LeetCode](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/append-characters-to-string-to-make-subsequence/) (Medium)

-   Tags: two pointers, string, greedy
## 2825. Make String a Subsequence Using Cyclic Increments

-   [LeetCode](https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/) | [LeetCode CH](https://leetcode.cn/problems/make-string-a-subsequence-using-cyclic-increments/) (Medium)

-   Tags: two pointers, string
## 1023. Camelcase Matching

-   [LeetCode](https://leetcode.com/problems/camelcase-matching/) | [LeetCode CH](https://leetcode.cn/problems/camelcase-matching/) (Medium)

-   Tags: array, two pointers, string, trie, string matching
## 3132. Find the Integer Added to Array II

-   [LeetCode](https://leetcode.com/problems/find-the-integer-added-to-array-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-the-integer-added-to-array-ii/) (Medium)

-   Tags: array, two pointers, sorting, enumeration
## 522. Longest Uncommon Subsequence II

-   [LeetCode](https://leetcode.com/problems/longest-uncommon-subsequence-ii/) | [LeetCode CH](https://leetcode.cn/problems/longest-uncommon-subsequence-ii/) (Medium)

-   Tags: array, hash table, two pointers, string, sorting
## 1898. Maximum Number of Removable Characters

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-removable-characters/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-removable-characters/) (Medium)

-   Tags: array, two pointers, string, binary search
## 2565. Subsequence With the Minimum Score

-   [LeetCode](https://leetcode.com/problems/subsequence-with-the-minimum-score/) | [LeetCode CH](https://leetcode.cn/problems/subsequence-with-the-minimum-score/) (Hard)

-   Tags: two pointers, string, binary search
## 3302. Find the Lexicographically Smallest Valid Sequence

-   [LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/) | [LeetCode CH](https://leetcode.cn/problems/find-the-lexicographically-smallest-valid-sequence/) (Medium)

-   Tags: two pointers, string, dynamic programming, greedy
