---
comments: True
---

# Valid Parentheses Strings

- [x] [20. Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/) (Easy)
- [ ] [921. Minimum Add to Make Parentheses Valid](https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/) (Medium)
- [ ] [1021. Remove Outermost Parentheses](https://leetcode.cn/problems/remove-outermost-parentheses/) (Easy)
- [ ] [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.cn/problems/maximum-nesting-depth-of-the-parentheses/) (Easy)
- [ ] [1190. Reverse Substrings Between Each Pair of Parentheses](https://leetcode.cn/problems/reverse-substrings-between-each-pair-of-parentheses/) (Medium)
- [ ] [856. Score of Parentheses](https://leetcode.cn/problems/score-of-parentheses/) (Medium)
- [ ] [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/) (Medium)
- [ ] [1963. Minimum Number of Swaps to Make the String Balanced](https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-string-balanced/) (Medium)
- [x] [678. Valid Parenthesis String](https://leetcode.cn/problems/valid-parenthesis-string/) (Medium)
- [ ] [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](https://leetcode.cn/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) (Medium)
- [ ] [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.cn/problems/minimum-insertions-to-balance-a-parentheses-string/) (Medium)
- [ ] [2116. Check if a Parentheses String Can Be Valid](https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/) (Medium)
- [ ] [32. Longest Valid Parentheses](https://leetcode.cn/problems/longest-valid-parentheses/) (Hard)

## 20. Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/valid-parentheses/) (Easy)

-   Tags: string, stack
-   Determine if the input string is valid.
-   Steps for the string `()[]{}`:

| char | action | stack |
| ---- | ------ | ----- |
| `(`  | push   | "\("  |
| `)`  | pop    | ""    |
| `[`  | push   | "\["  |
| `]`  | pop    | ""    |
| `{`  | push   | "\{"  |
| `}`  | pop    | ""    |

```python title="20. Valid Parentheses - Python Solution"
--8<-- "0020_valid_parentheses.py"
```

```cpp title="20. Valid Parentheses - C++ Solution"
--8<-- "cpp/0020_valid_parentheses.cc"
```

## 921. Minimum Add to Make Parentheses Valid

-   [LeetCode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | [LeetCode CH](https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/) (Medium)

-   Tags: string, stack, greedy

## 1021. Remove Outermost Parentheses

-   [LeetCode](https://leetcode.com/problems/remove-outermost-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/remove-outermost-parentheses/) (Easy)

-   Tags: string, stack

## 1614. Maximum Nesting Depth of the Parentheses

-   [LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/maximum-nesting-depth-of-the-parentheses/) (Easy)

-   Tags: string, stack

## 1190. Reverse Substrings Between Each Pair of Parentheses

-   [LeetCode](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/reverse-substrings-between-each-pair-of-parentheses/) (Medium)

-   Tags: string, stack

## 856. Score of Parentheses

-   [LeetCode](https://leetcode.com/problems/score-of-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/score-of-parentheses/) (Medium)

-   Tags: string, stack

## 1249. Minimum Remove to Make Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/minimum-remove-to-make-valid-parentheses/) (Medium)

-   Tags: string, stack

## 1963. Minimum Number of Swaps to Make the String Balanced

-   [LeetCode](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) | [LeetCode CH](https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-string-balanced/) (Medium)

-   Tags: two pointers, string, stack, greedy

## 678. Valid Parenthesis String

-   [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/) | [LeetCode CH](https://leetcode.cn/problems/valid-parenthesis-string/) (Medium)

-   Tags: string, dynamic programming, stack, greedy

```python title="678. Valid Parenthesis String - Python Solution"
--8<-- "0678_valid_parenthesis_string.py"
```

## 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

-   [LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) | [LeetCode CH](https://leetcode.cn/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) (Medium)

-   Tags: string, stack

## 1541. Minimum Insertions to Balance a Parentheses String

-   [LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) | [LeetCode CH](https://leetcode.cn/problems/minimum-insertions-to-balance-a-parentheses-string/) (Medium)

-   Tags: string, stack, greedy

## 2116. Check if a Parentheses String Can Be Valid

-   [LeetCode](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/) | [LeetCode CH](https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/) (Medium)

-   Tags: string, stack, greedy

## 32. Longest Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/longest-valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/longest-valid-parentheses/) (Hard)

-   Tags: string, dynamic programming, stack
