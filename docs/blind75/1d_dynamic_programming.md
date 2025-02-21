---
comments: True
---

# 1D Dynamic Programming

## 70. Climbing Stairs

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

## 198. House Robber

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
