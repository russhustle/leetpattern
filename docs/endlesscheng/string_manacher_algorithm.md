---
comments: True
---

# String Manacher Algorithm

- [x] [5. Longest Palindromic Substring](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)
- [x] [647. Palindromic Substrings](https://leetcode.cn/problems/palindromic-substrings/) (Medium)
- [x] [214. Shortest Palindrome](https://leetcode.cn/problems/shortest-palindrome/) (Hard)
- [ ] [3327. Check if DFS Strings Are Palindromes](https://leetcode.cn/problems/check-if-dfs-strings-are-palindromes/) (Hard)
- [ ] [1745. Palindrome Partitioning IV](https://leetcode.cn/problems/palindrome-partitioning-iv/) (Hard)
- [ ] [1960. Maximum Product of the Length of Two Palindromic Substrings](https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-substrings/) (Hard)

## 5. Longest Palindromic Substring

-   [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) | [LeetCode CH](https://leetcode.cn/problems/longest-palindromic-substring/) (Medium)

-   Tags: two pointers, string, dynamic programming
-   Return the longest palindromic substring in `s`.

```python title="5. Longest Palindromic Substring - Python Solution"
--8<-- "0005_longest_palindromic_substring.py"
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
--8<-- "0647_palindromic_substrings.py"
```

## 214. Shortest Palindrome

-   [LeetCode](https://leetcode.com/problems/shortest-palindrome/) | [LeetCode CH](https://leetcode.cn/problems/shortest-palindrome/) (Hard)

-   Tags: string, rolling hash, string matching, hash function

```python title="214. Shortest Palindrome - Python Solution"
--8<-- "0214_shortest_palindrome.py"
```

## 3327. Check if DFS Strings Are Palindromes

-   [LeetCode](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/) | [LeetCode CH](https://leetcode.cn/problems/check-if-dfs-strings-are-palindromes/) (Hard)

-   Tags: array, hash table, string, tree, depth first search, hash function

## 1745. Palindrome Partitioning IV

-   [LeetCode](https://leetcode.com/problems/palindrome-partitioning-iv/) | [LeetCode CH](https://leetcode.cn/problems/palindrome-partitioning-iv/) (Hard)

-   Tags: string, dynamic programming

## 1960. Maximum Product of the Length of Two Palindromic Substrings

-   [LeetCode](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/) | [LeetCode CH](https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-substrings/) (Hard)

-   Tags: string, rolling hash, hash function
