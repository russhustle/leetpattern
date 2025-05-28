---
comments: True
---

# DP Longest Palindromic Subsequence

## Table of Contents

- [x] [516. Longest Palindromic Subsequence](https://leetcode.cn/problems/longest-palindromic-subsequence/) (Medium)
- [ ] [730. Count Different Palindromic Subsequences](https://leetcode.cn/problems/count-different-palindromic-subsequences/) (Hard)
- [ ] [1312. Minimum Insertion Steps to Make a String Palindrome](https://leetcode.cn/problems/minimum-insertion-steps-to-make-a-string-palindrome/) (Hard)
- [ ] [1771. Maximize Palindrome Length From Subsequences](https://leetcode.cn/problems/maximize-palindrome-length-from-subsequences/) (Hard)
- [ ] [1682. Longest Palindromic Subsequence II](https://leetcode.cn/problems/longest-palindromic-subsequence-ii/) (Medium) 👑
- [ ] [1216. Valid Palindrome III](https://leetcode.cn/problems/valid-palindrome-iii/) (Hard) 👑
- [ ] [1246. Palindrome Removal](https://leetcode.cn/problems/palindrome-removal/) (Hard) 👑

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

## 730. Count Different Palindromic Subsequences

-   [LeetCode](https://leetcode.com/problems/count-different-palindromic-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/count-different-palindromic-subsequences/) (Hard)

-   Tags: string, dynamic programming
## 1312. Minimum Insertion Steps to Make a String Palindrome

-   [LeetCode](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/minimum-insertion-steps-to-make-a-string-palindrome/) (Hard)

-   Tags: string, dynamic programming
## 1771. Maximize Palindrome Length From Subsequences

-   [LeetCode](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/maximize-palindrome-length-from-subsequences/) (Hard)

-   Tags: string, dynamic programming
## 1682. Longest Palindromic Subsequence II

-   [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence-ii/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindromic-subsequence-ii/) (Medium)

-   Tags: string, dynamic programming
## 1216. Valid Palindrome III

-   [LeetCode](https://leetcode.com/problems/valid-palindrome-iii/) | [LeetCode CH](https://leetcode.cn/problems/valid-palindrome-iii/) (Hard)

-   Tags: string, dynamic programming
## 1246. Palindrome Removal

-   [LeetCode](https://leetcode.com/problems/palindrome-removal/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-removal/) (Hard)

-   Tags: array, dynamic programming
