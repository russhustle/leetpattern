---
comments: True
---

# Climbing Stairs

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

## 746. Min Cost Climbing Stairs

-   [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/) | [LeetCode CH](https://leetcode.cn/problems/min-cost-climbing-stairs/) (Easy)
-   Tags: array, dynamic programming
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

```python title="746. Min Cost Climbing Stairs"
--8<-- "0746_min_cost_climbing_stairs.py"
```

## 377. Combination Sum IV

-   [LeetCode](https://leetcode.com/problems/combination-sum-iv/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum-iv/) (Medium)
-   Tags: array, dynamic programming

```python title="377. Combination Sum IV"
--8<-- "0377_combination_sum_iv.py"
```

## 2466. Count Ways To Build Good Strings

-   [LeetCode](https://leetcode.com/problems/count-ways-to-build-good-strings/) | [LeetCode CH](https://leetcode.cn/problems/count-ways-to-build-good-strings/) (Medium)
-   Tags: dynamic programming


## 2266. Count Number of Texts

-   [LeetCode](https://leetcode.com/problems/count-number-of-texts/) | [LeetCode CH](https://leetcode.cn/problems/count-number-of-texts/) (Medium)
-   Tags: hash table, math, string, dynamic programming


## 2533. Number of Good Binary Strings

-   [LeetCode](https://leetcode.com/problems/number-of-good-binary-strings/) | [LeetCode CH](https://leetcode.cn/problems/number-of-good-binary-strings/) (Medium)
-   Tags: dynamic programming
