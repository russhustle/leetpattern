---
comments: True
---

# DP Interval

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

=== "Python"

    ```python
    --8<-- "0516_longest_palindromic_subsequence.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0516_longest_palindromic_subsequence.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0516_longest_palindromic_subsequence.ts"
    ```

## 647. Palindromic Substrings

-  [LeetCode](https://leetcode.com/problems/palindromic-substrings/) | [LeetCode CH](https://leetcode.cn/problems/palindromic-substrings/) (Medium)

-   Return the number of palindromic substrings in `s`.
-   Bottom-up DP table

|  dp   |  a  |  b  |  b  |  a  |  e  |
| :---: | :-: | :-: | :-: | :-: | :-: |
| **a** |  1  |  0  |  0  |  1  |  0  |
| **b** |  0  |  1  |  1  |  0  |  0  |
| **b** |  0  |  0  |  1  |  0  |  0  |
| **a** |  0  |  0  |  0  |  1  |  0  |
| **e** |  0  |  0  |  0  |  0  |  1  |

=== "Python"

    ```python
    --8<-- "0647_palindromic_substrings.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0647_palindromic_substrings.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0647_palindromic_substrings.ts"
    ```

## 5. Longest Palindromic Substring

-  [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)

-   Return the longest palindromic substring in `s`.

=== "Python"

    ```python
    --8<-- "0005_longest_palindromic_substring.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0005_longest_palindromic_substring.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0005_longest_palindromic_substring.ts"
    ```
