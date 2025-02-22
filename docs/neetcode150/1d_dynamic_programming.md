---
comments: True
---

# 1D Dynamic Programming

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

## 746. Min Cost Climbing Stairs

-  [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/) | [LeetCode CH](https://leetcode.cn/problems/min-cost-climbing-stairs/) (Easy)

-   Return the minimum cost to reach the top of the stairs.

-   `dp[n]` stores the <u>minimum cost</u> to reach the `n-th` stair.
-   Formula: `dp[n] = cost[n] + min(dp[n - 1], dp[n - 2])`.
-   Initialize `dp[0] = cost[0]` and `dp[1] = cost[1]`.
-   Return `min(dp[-1], dp[-2])`.

-   Example: `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`

|  n  | `cost[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----: |
|  0  |     1     |     -     |     -     |    1    |
|  1  |    100    |     -     |     1     |   100   |
|  2  |     1     |     1     |    100    |    2    |
|  3  |     1     |    100    |     2     |    3    |
|  4  |     1     |     2     |     3     |    3    |
|  5  |    100    |     3     |     3     |   103   |
|  6  |     1     |     3     |    103    |    4    |
|  7  |     1     |    103    |     4     |    5    |
|  8  |    100    |     4     |     5     |   104   |
|  9  |     1     |     5     |    104    |    6    |

=== "Python"

    ```python
    --8<-- "0746_min_cost_climbing_stairs.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0746_min_cost_climbing_stairs.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0746_min_cost_climbing_stairs.ts"
    ```

## 198. House Robber

-  [LeetCode](https://leetcode.com/problems/house-robber/) | [LeetCode CH](https://leetcode.cn/problems/house-robber/) (Medium)

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

=== "Python"

    ```python
    --8<-- "0198_house_robber.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0198_house_robber.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0198_house_robber.ts"
    ```

## 213. House Robber II

-  [LeetCode](https://leetcode.com/problems/house-robber-ii/) | [LeetCode CH](https://leetcode.cn/problems/house-robber-ii/) (Medium)

-   Return the maximum amount of money that can be robbed from the houses arranged in a circle.
-   Circular → Linear: `nums[0]` and `nums[-1]` cannot be robbed together.
-   Rob from `0` to `n - 2`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  0  |     2     |     -     |     2     |          -          |    2    |
|  1  |     7     |     -     |     7     |          -          |    7    |
|  2  |     9     |     2     |     7     |         11          |   11    |
|  3  |     3     |     7     |    11     |         10          |   11    |

-   Rob from `1` to `n - 1`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  1  |     7     |     -     |     -     |          -          |    7    |
|  2  |     9     |     -     |     7     |          -          |    9    |
|  3  |     3     |     7     |     9     |         10          |   10    |
|  4  |     1     |     9     |    10     |         10          |   10    |

=== "Python"

    ```python
    --8<-- "0213_house_robber_ii.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0213_house_robber_ii.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0213_house_robber_ii.ts"
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

## 91. Decode Ways

-  [LeetCode](https://leetcode.com/problems/decode-ways/) | [LeetCode CH](https://leetcode.cn/problems/decode-ways/) (Medium)

=== "Python"

    ```python
    --8<-- "0091_decode_ways.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0091_decode_ways.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0091_decode_ways.ts"
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

## 152. Maximum Product Subarray

-  [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-product-subarray/) (Medium)

=== "Python"

    ```python
    --8<-- "0152_maximum_product_subarray.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0152_maximum_product_subarray.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0152_maximum_product_subarray.ts"
    ```

## 139. Word Break

-  [LeetCode](https://leetcode.com/problems/word-break/) | [LeetCode CH](https://leetcode.cn/problems/word-break/) (Medium)

=== "Python"

    ```python
    --8<-- "0139_word_break.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0139_word_break.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0139_word_break.ts"
    ```

## 300. Longest Increasing Subsequence

-  [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/longest-increasing-subsequence/) (Medium)

=== "Python"

    ```python
    --8<-- "0300_longest_increasing_subsequence.py"
    ```

=== "C++"

    ```cpp
    --8<-- "cpp/0300_longest_increasing_subsequence.cc"
    ```

=== "TypeScript"

    ```typescript
    --8<-- "ts/0300_longest_increasing_subsequence.ts"
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
