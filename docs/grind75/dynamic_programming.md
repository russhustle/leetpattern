---
comments: True
---

# Dynamic Programming

- [x] [70. Climbing Stairs](https://leetcode.cn/problems/climbing-stairs/) (Easy)
- [x] [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) (Medium)
- [x] [322. Coin Change](https://leetcode.cn/problems/coin-change/) (Medium)
- [x] [416. Partition Equal Subset Sum](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)
- [x] [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) (Medium)

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

```python title="70. Climbing Stairs"
--8<-- "0070_climbing_stairs.py"
```

## 53. Maximum Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray/) (Medium)
-   Tags: array, divide and conquer, dynamic programming

```python title="53. Maximum Subarray"
--8<-- "0053_maximum_subarray.py"
```

## 322. Coin Change

-   [LeetCode](https://leetcode.com/problems/coin-change/) | [LeetCode CH](https://leetcode.cn/problems/coin-change/) (Medium)
-   Tags: array, dynamic programming, breadth first search

```python title="322. Coin Change"
--8<-- "0322_coin_change.py"
```

## 416. Partition Equal Subset Sum

-   [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) | [LeetCode CH](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)
-   Tags: array, dynamic programming

```python title="416. Partition Equal Subset Sum"
--8<-- "0416_partition_equal_subset_sum.py"
```

## 62. Unique Paths

-   [LeetCode](https://leetcode.com/problems/unique-paths/) | [LeetCode CH](https://leetcode.cn/problems/unique-paths/) (Medium)
-   Tags: math, dynamic programming, combinatorics
-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid.

![62](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```python title="62. Unique Paths"
--8<-- "0062_unique_paths.py"
```
