---
comments: True
---

# DP Basic

- [x] [509. Fibonacci Number](https://leetcode.cn/problems/fibonacci-number/) (Easy)
- [x] [70. Climbing Stairs](https://leetcode.cn/problems/climbing-stairs/) (Easy)
- [x] [746. Min Cost Climbing Stairs](https://leetcode.cn/problems/min-cost-climbing-stairs/) (Easy)
- [x] [198. House Robber](https://leetcode.cn/problems/house-robber/) (Medium)
- [x] [213. House Robber II](https://leetcode.cn/problems/house-robber-ii/) (Medium)
- [x] [376. Wiggle Subsequence](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)
- [x] [343. Integer Break](https://leetcode.cn/problems/integer-break/) (Medium)
- [x] [1025. Divisor Game](https://leetcode.cn/problems/divisor-game/) (Easy)

## 509. Fibonacci Number

-   [LeetCode](https://leetcode.com/problems/fibonacci-number/) | [LeetCode CH](https://leetcode.cn/problems/fibonacci-number/) (Easy)

-   Tags: math, dynamic programming, recursion, memoization
-   Return the `n-th` Fibonacci number.
-   `dp[n]` stores the `n-th` Fibonacci number.
-   Formula: `dp[n] = dp[n - 1] + dp[n - 2]`.
-   Initialize `dp[0] = 0` and `dp[1] = 1`.

|  n  | `dp[n-2]` | `dp[n-1]` | `dp[n]` |
| :-: | :-------: | :-------: | :-----: |
|  0  |     -     |     -     |    0    |
|  1  |     -     |     0     |    1    |
|  2  |     0     |     1     |    1    |
|  3  |     1     |     1     |    2    |
|  4  |     1     |     2     |    3    |
|  5  |     2     |     3     |    5    |
|  6  |     3     |     5     |    8    |
|  7  |     5     |     8     |   13    |
|  8  |     8     |    13     |   21    |
|  9  |    13     |    21     |   34    |
| 10  |    21     |    34     |   55    |

```python title="509. Fibonacci Number - Python Solution"
--8<-- "0509_fibonacci_number.py"
```

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

```python title="746. Min Cost Climbing Stairs - Python Solution"
--8<-- "0746_min_cost_climbing_stairs.py"
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

## 213. House Robber II

-   [LeetCode](https://leetcode.com/problems/house-robber-ii/) | [LeetCode CH](https://leetcode.cn/problems/house-robber-ii/) (Medium)

-   Tags: array, dynamic programming
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

```python title="213. House Robber II - Python Solution"
--8<-- "0213_house_robber_ii.py"
```

## 376. Wiggle Subsequence

-   [LeetCode](https://leetcode.com/problems/wiggle-subsequence/) | [LeetCode CH](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)

-   Tags: array, dynamic programming, greedy
-   Return the length of the longest wiggle subsequence.
-   `up[n]` stores the length of the longest wiggle subsequence ending at `n` with a rising wiggle.
-   `down[n]` stores the length of the longest wiggle subsequence ending at `n` with a falling wiggle.
-   Initialize `up[0] = 1` and `down[0] = 1`.
-   Example: `nums = [1, 7, 4, 9, 2, 5]`

| `nums[n]` | `nums[n-1]` | `up[n-1]` | `down[n-1]` | `up[n]` | `down[n]` |
| :-------: | :---------: | :-------: | :---------: | :-----: | :-------: |
|     1     |      -      |     -     |      -      |    1    |     1     |
|     7     |      1      |     1     |      1      |    2    |     1     |
|     4     |      7      |     2     |      1      |    2    |     3     |
|     9     |      4      |     2     |      3      |    4    |     3     |
|     2     |      9      |     4     |      3      |    4    |     5     |
|     5     |      2      |     4     |      5      |    6    |     5     |

```python title="376. Wiggle Subsequence - Python Solution"
--8<-- "0376_wiggle_subsequence.py"
```

## 343. Integer Break

-   [LeetCode](https://leetcode.com/problems/integer-break/) | [LeetCode CH](https://leetcode.cn/problems/integer-break/) (Medium)

-   Tags: math, dynamic programming
-   Return the maximum product of the integer after breaking it into at least two positive integers.
-   `dp[i]` stores the maximum product of the integer `i`.
-   Formula: `dp[i] = max(dp[i - j] * j, (i - j) * j)`

|    dp    |   3    |   4    |   5    |   6    |    7    |    8     |
| :------: | :----: | :----: | :----: | :----: | :-----: | :------: |
|    2     | 2\*1=2 | 2\*2=4 | 2\*3=6 | 2\*4=8 | 2\*5=10 | 2\*6=12  |
| dp[2]=1  | 1\*1=2 | 1\*2=2 | 1\*3=3 | 1\*4=4 | 1\*5=5  |  1\*6=6  |
|    3     |        | 3\*1=3 | 3\*2=6 | 3\*3=9 | 3\*4=12 | 3\*5=15  |
| dp[3]=2  |        | 2\*1=2 | 2\*2=4 | 2\*3=6 | 2\*4=8  | 2\*5=10  |
|    4     |        |        | 4\*1=4 | 4\*2=8 | 4\*3=12 | 4\*4=16  |
| dp[4]=4  |        |        | 4\*1=4 | 4\*2=8 | 4\*3=12 | 4\*4=16  |
|    5     |        |        |        | 5\*1=5 | 5\*2=10 | 5\*3=15  |
| dp[5]=6  |        |        |        | 6\*1=6 | 6\*2=12 | 6\*3=18  |
|    6     |        |        |        |        | 6\*1=6  | 6\*2=12  |
| dp[6]=9  |        |        |        |        | 9\*1=9  | 9\*2=18  |
|    7     |        |        |        |        |         |  7\*1=7  |
| dp[7]=12 |        |        |        |        |         | 12\*1=12 |
| `dp[n]`  |   2    |   4    |   6    |   9    |   12    |    18    |

```python title="343. Integer Break - Python Solution"
--8<-- "0343_integer_break.py"
```

## 1025. Divisor Game

-   [LeetCode](https://leetcode.com/problems/divisor-game/) | [LeetCode CH](https://leetcode.cn/problems/divisor-game/) (Easy)

-   Tags: math, dynamic programming, brainteaser, game theory
-   Return `True` if Alice wins the game, assuming both players play optimally.
-   `dp[n]` stores the result of the game when the number is `n`.
-   Initialize `dp[1] = False`.

```python title="1025. Divisor Game - Python Solution"
--8<-- "1025_divisor_game.py"
```
