---
comments: true
---

# Dynamic Programming - Basic

## LeetCode Problems

1. 0509 - [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | [斐波那契数](https://leetcode.cn/problems/fibonacci-number/) (Easy)
2. 0070 - [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | [爬楼梯](https://leetcode.cn/problems/climbing-stairs/) (Easy)
3. 0746 - [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | [使用最小花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs/) (Easy)
4. 0198 - [House Robber](https://leetcode.com/problems/house-robber/) | [打家劫舍](https://leetcode.cn/problems/house-robber/) (Easy)
5. 0213 - [House Robber II](https://leetcode.com/problems/house-robber-ii/) | [打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/) (Medium)
6. 0376 - [Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/) | [摆动序列](https://leetcode.cn/problems/wiggle-subsequence/) (Medium)
7. 0343 - [Integer Break](https://leetcode.com/problems/integer-break/) | [整数拆分](https://leetcode.cn/problems/integer-break/) (Medium)
8. 1025 - [Divisor Game](https://leetcode.com/problems/divisor-game/) | [除数博弈](https://leetcode.cn/problems/divisor-game/) (Easy)

## 509. Fibonacci Number

-   Return the `n-th` Fibonacci number.

```python
--8<-- "0509_fibonacci_number.py"
```

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

## 70. Climbing Stairs

-   Return the number of distinct ways to reach the top of the stairs.

```python
--8<-- "0070_climbing_stairs.py"
```

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

## 746. Min Cost Climbing Stairs

-   Return the minimum cost to reach the top of the stairs.

```python
--8<-- "0746_min_cost_climbing_stairs.py"
```

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

## 198. House Robber

-   Return the maximum amount of money that can be robbed from the houses. No two adjacent houses can be robbed.

```python
--8<-- "0198_house_robber.py"
```

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

## 213. House Robber II

-   Return the maximum amount of money that can be robbed from the houses arranged in a circle.

```python
--8<-- "0213_house_robber_ii.py"
```

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

## 376. Wiggle Subsequence

-   Return the length of the longest wiggle subsequence.

```python
--8<-- "0376_wiggle_subsequence.py"
```

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

## 343. Integer Break

-   Return the maximum product of the integer after breaking it into at least two positive integers.

```python
--8<-- "0343_integer_break.py"
```

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

## 1025. Divisor Game

-   Return `True` if Alice wins the game, assuming both players play optimally.

```python
--8<-- "1025_divisor_game.py"
```

-   `dp[n]` stores the result of the game when the number is `n`.
-   Initialize `dp[1] = False`.
