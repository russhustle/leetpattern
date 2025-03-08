---
comments: True
---

# Dynamic Programming

- [x] [70. Climbing Stairs](https://leetcode.cn/problems/climbing-stairs/) (Easy)
- [x] [118. Pascal's Triangle](https://leetcode.cn/problems/pascals-triangle/) (Easy)
- [x] [198. House Robber](https://leetcode.cn/problems/house-robber/) (Medium)
- [x] [279. Perfect Squares](https://leetcode.cn/problems/perfect-squares/) (Medium)
- [x] [322. Coin Change](https://leetcode.cn/problems/coin-change/) (Medium)
- [x] [139. Word Break](https://leetcode.cn/problems/word-break/) (Medium)
- [x] [300. Longest Increasing Subsequence](https://leetcode.cn/problems/longest-increasing-subsequence/) (Medium)
- [x] [152. Maximum Product Subarray](https://leetcode.cn/problems/maximum-product-subarray/) (Medium)
- [x] [416. Partition Equal Subset Sum](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)
- [ ] [32. Longest Valid Parentheses](https://leetcode.cn/problems/longest-valid-parentheses/) (Hard)

## 70. Climbing Stairs

-   [LeetCode](https://leetcode.com/problems/climbing-stairs/) | [LeetCode CH](https://leetcode.cn/problems/climbing-stairs/) (Easy)

-   Tags: math, dynamic programming, memoization
-   Return the number of distinct ways to reach the top of the stairs.
-   `dp[n]` stores the number of distinct ways to reach the `n-th` stair.
-   Formula: `dp[n] = dp[n - 1] + dp[n - 2]`.
-   Initialize `dp[0] = 0`, `dp[1] = 1`, and `dp[2] = 2`.

|  n  | `dp[n-2]` | `dp[n-1]` | `dp[n]` |
| :-: | :-------: | :-------: | :-----: |
|  0  |     -     |     -     |    0    |
|  1  |     -     |     -     |    1    |
|  2  |     -     |     1     |    2    |
|  3  |     1     |     2     |    3    |
|  4  |     2     |     3     |    5    |
|  5  |     3     |     5     |    8    |
|  6  |     5     |     8     |   13    |
|  7  |     8     |    13     |   21    |
|  8  |    13     |    21     |   34    |
|  9  |    21     |    34     |   55    |
| 10  |    34     |    55     |   89    |

```python title="70. Climbing Stairs - Python Solution"
--8<-- "0070_climbing_stairs.py"
```

```cpp title="70. Climbing Stairs - C++ Solution"
--8<-- "cpp/0070_climbing_stairs.cc"
```

## 118. Pascal's Triangle

-   [LeetCode](https://leetcode.com/problems/pascals-triangle/) | [LeetCode CH](https://leetcode.cn/problems/pascals-triangle/) (Easy)

-   Tags: array, dynamic programming
-   Generate the first `numRows` of Pascal's triangle.

```plaintext
                 numRows    index
     1              1         0
    1 1             2         1
   1 2 1            3         2
  1 3 3 1           4         3
 1 4 6 4 1          5         4
```

```python title="118. Pascal's Triangle - Python Solution"
--8<-- "0118_pascals_triangle.py"
```

## 198. House Robber

-   [LeetCode](https://leetcode.com/problems/house-robber/) | [LeetCode CH](https://leetcode.cn/problems/house-robber/) (Medium)

-   Tags: array, dynamic programming
-   Return the maximum amount of money that can be robbed from the houses. No two adjacent houses can be robbed.

-   `dp[n]` stores the maximum amount of money that can be robbed from the first `n` houses.
-   Formula: `dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])`.
    -   Skip: `dp[n]` → `dp[n - 1]`
    -   Rob: `dp[n]` → `dp[n - 2] + nums[n]`
-   Initialize `dp[0] = nums[0]` and `dp[1] = max(nums[0], nums[1])`.
-   Return `dp[-1]`.
-   Example: `nums = [2, 7, 9, 3, 1]`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  0  |     2     |     -     |     2     |          -          |    2    |
|  1  |     7     |     -     |     7     |          -          |    7    |
|  2  |     9     |     2     |     7     |         11          |   11    |
|  3  |     3     |     7     |    11     |         10          |   11    |
|  4  |     1     |    11     |    11     |         12          |   12    |

```python title="198. House Robber - Python Solution"
--8<-- "0198_house_robber.py"
```

```cpp title="198. House Robber - C++ Solution"
--8<-- "cpp/0198_house_robber.cc"
```

## 279. Perfect Squares

-   [LeetCode](https://leetcode.com/problems/perfect-squares/) | [LeetCode CH](https://leetcode.cn/problems/perfect-squares/) (Medium)

-   Tags: math, dynamic programming, breadth first search

```python title="279. Perfect Squares - Python Solution"
--8<-- "0279_perfect_squares.py"
```

## 322. Coin Change

-   [LeetCode](https://leetcode.com/problems/coin-change/) | [LeetCode CH](https://leetcode.cn/problems/coin-change/) (Medium)

-   Tags: array, dynamic programming, breadth first search

```python title="322. Coin Change - Python Solution"
--8<-- "0322_coin_change.py"
```

## 139. Word Break

-   [LeetCode](https://leetcode.com/problems/word-break/) | [LeetCode CH](https://leetcode.cn/problems/word-break/) (Medium)

-   Tags: array, hash table, string, dynamic programming, trie, memoization

```python title="139. Word Break - Python Solution"
--8<-- "0139_word_break.py"
```

## 300. Longest Increasing Subsequence

-   [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-increasing-subsequence/) (Medium)

-   Tags: array, binary search, dynamic programming

```python title="300. Longest Increasing Subsequence - Python Solution"
--8<-- "0300_longest_increasing_subsequence.py"
```

## 152. Maximum Product Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-product-subarray/) (Medium)

-   Tags: array, dynamic programming

```python title="152. Maximum Product Subarray - Python Solution"
--8<-- "0152_maximum_product_subarray.py"
```

## 416. Partition Equal Subset Sum

-   [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) | [LeetCode CH](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)

-   Tags: array, dynamic programming

```python title="416. Partition Equal Subset Sum - Python Solution"
--8<-- "0416_partition_equal_subset_sum.py"
```

## 32. Longest Valid Parentheses

-   [LeetCode](https://leetcode.com/problems/longest-valid-parentheses/) | [LeetCode CH](https://leetcode.cn/problems/longest-valid-parentheses/) (Hard)

-   Tags: string, dynamic programming, stack
