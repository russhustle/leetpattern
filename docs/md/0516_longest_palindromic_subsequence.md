## 516. Longest Palindromic Subsequence

-  [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindromic-subsequence/) (Medium)

-   Return the length of the longest palindromic subsequence in `s`.
-   Bottom-up DP table

| dp  |  b  |  b  |  b  |        a         |      b       |
| :-: | :-: | :-: | :-: | :--------------: | :----------: |
|  b  |  1  |  2  |  3  |        3         |      4       |
|  b  |  0  |  1  |  2  |        2         | 3 `dp[i][j]` |
|  b  |  0  |  0  |  1  | 1 `dp[i+1][j-1]` |      2       |
|  a  |  0  |  0  |  0  |        1         |      1       |
|  b  |  0  |  0  |  0  |        0         |      1       |
