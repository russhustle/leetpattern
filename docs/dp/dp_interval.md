# Dynamic Programming - Interval

## LeetCode Problems

1. 0516 - [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) (Medium)
2. 0647 - [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) (Medium)
3. 0005 - [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (Medium)

## 516. Longest Palindromic Subsequence

-   Return the length of the longest palindromic subsequence in `s`.

```python
--8<-- "0516_longest_palindromic_subsequence.py"
```

-   Bottom-up DP table

| dp  |  b  |  b  |  b  |        a         |      b       |
| :-: | :-: | :-: | :-: | :--------------: | :----------: |
|  b  |  1  |  2  |  3  |        3         |      4       |
|  b  |  0  |  1  |  2  |        2         | 3 `dp[i][j]` |
|  b  |  0  |  0  |  1  | 1 `dp[i+1][j-1]` |      2       |
|  a  |  0  |  0  |  0  |        1         |      1       |
|  b  |  0  |  0  |  0  |        0         |      1       |

## 647. Palindromic Substrings

-   Return the number of palindromic substrings in `s`.

```python
--8<-- "0647_palindromic_substrings.py"
```

-   Bottom-up DP table

|  dp   |  a   |  b   |  b   |  a   |  e   |
| :---: | :--: | :--: | :--: | :--: | :--: |
| **a** |  1   |  0   |  0   |  1   |  0   |
| **b** |  0   |  1   |  1   |  0   |  0   |
| **b** |  0   |  0   |  1   |  0   |  0   |
| **a** |  0   |  0   |  0   |  1   |  0   |
| **e** |  0   |  0   |  0   |  0   |  1   |

## 5. Longest Palindromic Substring

-   Return the longest palindromic substring in `s`.

```python
--8<-- "0005_longest_palindromic_substring.py"
```
