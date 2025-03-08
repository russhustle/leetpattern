---
comments: True
---

# DP Matrix Exponentiation Optimized

- [x] [70. Climbing Stairs](https://leetcode.cn/problems/climbing-stairs/) (Easy)
- [x] [509. Fibonacci Number](https://leetcode.cn/problems/fibonacci-number/) (Easy)
- [ ] [1137. N-th Tribonacci Number](https://leetcode.cn/problems/n-th-tribonacci-number/) (Easy)
- [ ] [1220. Count Vowels Permutation](https://leetcode.cn/problems/count-vowels-permutation/) (Hard)
- [ ] [552. Student Attendance Record II](https://leetcode.cn/problems/student-attendance-record-ii/) (Hard)
- [ ] [935. Knight Dialer](https://leetcode.cn/problems/knight-dialer/) (Medium)
- [ ] [790. Domino and Tromino Tiling](https://leetcode.cn/problems/domino-and-tromino-tiling/) (Medium)
- [ ] [3337. Total Characters in String After Transformations II](https://leetcode.cn/problems/total-characters-in-string-after-transformations-ii/) (Hard)
- [ ] [2851. String Transformation](https://leetcode.cn/problems/string-transformation/) (Hard)
- [ ] [2912. Number of Ways to Reach Destination in the Grid](https://leetcode.cn/problems/number-of-ways-to-reach-destination-in-the-grid/) (Hard) 👑

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

## 1137. N-th Tribonacci Number

-   [LeetCode](https://leetcode.com/problems/n-th-tribonacci-number/) | [LeetCode CH](https://leetcode.cn/problems/n-th-tribonacci-number/) (Easy)

-   Tags: math, dynamic programming, memoization

## 1220. Count Vowels Permutation

-   [LeetCode](https://leetcode.com/problems/count-vowels-permutation/) | [LeetCode CH](https://leetcode.cn/problems/count-vowels-permutation/) (Hard)

-   Tags: dynamic programming

## 552. Student Attendance Record II

-   [LeetCode](https://leetcode.com/problems/student-attendance-record-ii/) | [LeetCode CH](https://leetcode.cn/problems/student-attendance-record-ii/) (Hard)

-   Tags: dynamic programming

## 935. Knight Dialer

-   [LeetCode](https://leetcode.com/problems/knight-dialer/) | [LeetCode CH](https://leetcode.cn/problems/knight-dialer/) (Medium)

-   Tags: dynamic programming

## 790. Domino and Tromino Tiling

-   [LeetCode](https://leetcode.com/problems/domino-and-tromino-tiling/) | [LeetCode CH](https://leetcode.cn/problems/domino-and-tromino-tiling/) (Medium)

-   Tags: dynamic programming

## 3337. Total Characters in String After Transformations II

-   [LeetCode](https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/) | [LeetCode CH](https://leetcode.cn/problems/total-characters-in-string-after-transformations-ii/) (Hard)

-   Tags: hash table, math, string, dynamic programming, counting

## 2851. String Transformation

-   [LeetCode](https://leetcode.com/problems/string-transformation/) | [LeetCode CH](https://leetcode.cn/problems/string-transformation/) (Hard)

-   Tags: math, string, dynamic programming, string matching

## 2912. Number of Ways to Reach Destination in the Grid

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-reach-destination-in-the-grid/) (Hard)

-   Tags: math, dynamic programming, combinatorics
