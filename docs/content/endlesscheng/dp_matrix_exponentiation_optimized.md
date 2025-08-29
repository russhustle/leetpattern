---
comments: True
---

# DP Matrix Exponentiation Optimized

## Table of Contents

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
- Return the number of distinct ways to reach the top of the stairs.
- `dp[n]` stores the number of distinct ways to reach the `n-th` stair.
- Formula: `dp[n] = dp[n - 1] + dp[n - 2]`.
- Initialize `dp[0] = 0`, `dp[1] = 1`, and `dp[2] = 2`.

```python title="70. Climbing Stairs - Python Solution"
from functools import cache


# DP
def climbStairsDP(n: int) -> int:
    if n <= 2:
        return n

    dp = [i for i in range(n + 1)]

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# DP (Optimized)
def climbStairsDPOptimized(n: int) -> int:
    if n <= 2:
        return n

    first, second = 1, 2

    for _ in range(3, n + 1):
        first, second = second, first + second

    return second


# Recursion
def climbStairsRecursion(n: int) -> int:
    @cache
    def dfs(i: int) -> int:
        if i <= 1:
            return 1
        return dfs(i - 1) + dfs(i - 2)

    return dfs(n)


# Greedy
def climbStairsGreedy(n: int) -> int:
    if n <= 2:
        return n

    p1, p2 = 1, 2

    for _ in range(3, n + 1):
        p1, p2 = p2, p1 + p2

    return p2


if __name__ == "__main__":
    assert climbStairsDP(10) == 89
    assert climbStairsDPOptimized(10) == 89
    assert climbStairsRecursion(10) == 89
    assert climbStairsGreedy(10) == 89

```

```cpp title="70. Climbing Stairs - C++ Solution"
#include <iostream>
using namespace std;

int climbStairs(int n) {
    if (n <= 2) return n;
    int f1 = 1, f2 = 2;
    int res;

    int i = 3;
    while (i <= n) {
        res = f1 + f2;
        f1 = f2;
        f2 = res;
        ++i;
    }
    return res;
}

int main() {
    cout << climbStairs(2) << endl;  // 2
    cout << climbStairs(3) << endl;  // 3
    cout << climbStairs(6) << endl;  // 13
    return 0;
}
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
from functools import cache


# DP
def fibDP(n: int) -> int:
    if n <= 1:
        return n

    dp = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# DP (Optimized)
def fibDPOptimized(n: int) -> int:
    if n <= 1:
        return n

    n1, n2 = 0, 1
    for _ in range(2, n + 1):
        n1, n2 = n2, n1 + n2

    return n2


# Recursive
@cache
def fibRecursive(n: int) -> int:
    if n <= 1:
        return n

    return fibRecursive(n - 1) + fibRecursive(n - 2)


n = 10
print(fibDP(n))  # 55
print(fibDPOptimized(n))  # 55
print(fibRecursive(n))  # 55

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
