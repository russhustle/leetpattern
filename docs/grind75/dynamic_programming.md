---
comments: True
---

# Dynamic Programming

## 70. Climbing Stairs

-  [LeetCode](https://leetcode.com/problems/climbing-stairs/) | [LeetCode CH](https://leetcode.cn/problems/climbing-stairs/) (Easy)

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

=== "Python"

    ```python
    --8<-- "0070_climbing_stairs.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0070_climbing_stairs.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0070_climbing_stairs.ts"
    ```

## 53. Maximum Subarray

-  [LeetCode](https://leetcode.com/problems/maximum-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray/) (Medium)

=== "Python"

    ```python
    --8<-- "0053_maximum_subarray.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0053_maximum_subarray.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0053_maximum_subarray.ts"
    ```

## 322. Coin Change

-  [LeetCode](https://leetcode.com/problems/coin-change/) | [LeetCode CH](https://leetcode.cn/problems/coin-change/) (Medium)

=== "Python"

    ```python
    --8<-- "0322_coin_change.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0322_coin_change.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0322_coin_change.ts"
    ```

## 416. Partition Equal Subset Sum

-  [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) | [LeetCode CH](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)

=== "Python"

    ```python
    --8<-- "0416_partition_equal_subset_sum.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0416_partition_equal_subset_sum.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0416_partition_equal_subset_sum.ts"
    ```

## 62. Unique Paths

-  [LeetCode](https://leetcode.com/problems/unique-paths/) | [LeetCode CH](https://leetcode.cn/problems/unique-paths/) (Medium)

-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid.

![62](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

=== "Python"

    ```python
    --8<-- "0062_unique_paths.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0062_unique_paths.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0062_unique_paths.ts"
    ```
