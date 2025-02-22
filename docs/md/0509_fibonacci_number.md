## 509. Fibonacci Number

-  [LeetCode](https://leetcode.com/problems/fibonacci-number/) | [LeetCode CH](https://leetcode.cn/problems/fibonacci-number/) (Easy)

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
