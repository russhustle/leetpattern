---
comments: True
---

# DP Climbing Stairs

## Table of Contents

- [x] [70. Climbing Stairs](https://leetcode.cn/problems/climbing-stairs/) (Easy)
- [x] [746. Min Cost Climbing Stairs](https://leetcode.cn/problems/min-cost-climbing-stairs/) (Easy)
- [x] [377. Combination Sum IV](https://leetcode.cn/problems/combination-sum-iv/) (Medium)
- [ ] [2466. Count Ways To Build Good Strings](https://leetcode.cn/problems/count-ways-to-build-good-strings/) (Medium)
- [ ] [2266. Count Number of Texts](https://leetcode.cn/problems/count-number-of-texts/) (Medium)
- [ ] [2533. Number of Good Binary Strings](https://leetcode.cn/problems/number-of-good-binary-strings/) (Medium) 👑

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
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    dp = [0 for _ in range(len(cost))]

    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    print(dp)
    return min(dp[-1], dp[-2])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))  # 6

```

## 377. Combination Sum IV

-   [LeetCode](https://leetcode.com/problems/combination-sum-iv/) | [LeetCode CH](https://leetcode.cn/problems/combination-sum-iv/) (Medium)

-   Tags: array, dynamic programming

```python title="377. Combination Sum IV - Python Solution"
from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1

    for i in range(1, target + 1):
        for j in range(len(nums)):
            if i - nums[j] >= 0:
                dp[i] += dp[i - nums[j]]

        return dp[target]


nums = [1, 2, 3]
target = 4
print(combinationSum4(nums, target))  # 7

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
