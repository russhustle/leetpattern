---
comments: True
---

# DP Basic

## Table of Contents

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
from typing import List


# DP (House Robber)
def rob1(nums: List[int]) -> int:
    if len(nums) < 3:
        return max(nums)

    dp = [0 for _ in range(len(nums))]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


# DP (House Robber) Optimized
def rob2(nums: List[int]) -> int:
    f0, f1 = 0, 0

    for num in nums:
        f0, f1 = f1, max(f1, f0 + num)

    return f1


nums = [2, 7, 9, 3, 1]
print(rob1(nums))  # 12
print(rob2(nums))  # 12

```

```cpp title="198. House Robber - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

int rob(vector<int> &nums) {
    int prev = 0, cur = 0, temp = 0;

    for (int num : nums) {
        temp = cur;
        cur = max(cur, prev + num);
        prev = temp;
    }
    return cur;
}

int main() {
    vector<int> nums = {2, 7, 9, 3, 1};
    cout << rob(nums) << endl;  // 12
    return 0;
}
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
from typing import List


# DP
def rob(nums: List[int]) -> int:
    if len(nums) <= 3:
        return max(nums)

    def robLinear(nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    # circle -> linear
    a = robLinear(nums[1:])  # 2nd house to the last house
    b = robLinear(nums[:-1])  # 1st house to the 2nd last house

    return max(a, b)


nums = [2, 7, 9, 3, 1]
print(rob(nums))  # 11

```

```cpp title="213. House Robber II - C++ Solution"
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// DP
int robDP(vector<int>& nums) {
    int n = nums.size();
    if (n <= 3) return *max_element(nums.begin(), nums.end());

    vector<int> dp1(n, 0), dp2(n, 0);

    dp1[0] = nums[0];
    dp2[1] = max(nums[0], nums[1]);
    for (int i = 2; i < n - 1; i++) {
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
    }

    dp2[1] = nums[1];
    dp2[2] = max(nums[1], nums[2]);
    for (int i = 3; i < n; i++) {
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i]);
    }

    return max(dp1[n - 2], dp2[n - 1]);
}

// DP (Space Optimized)
int robDPOptimized(vector<int>& nums) {
    int n = nums.size();
    if (n <= 3) return *max_element(nums.begin(), nums.end());

    int f1 = nums[0];
    int f2 = max(nums[0], nums[1]);
    int res1;
    for (int i = 2; i < n - 1; i++) {
        res1 = max(f2, f1 + nums[i]);
        f1 = f2;
        f2 = res1;
    }

    f1 = nums[1];
    f2 = max(nums[1], nums[2]);
    int res2;
    for (int i = 3; i < n; i++) {
        res2 = max(f2, f1 + nums[i]);
        f1 = f2;
        f2 = res2;
    }

    return max(res1, res2);
}

int main() {
    vector<int> nums = {2, 3, 2};
    cout << robDP(nums) << endl;           // 3
    cout << robDPOptimized(nums) << endl;  // 3

    nums = {1, 2, 3, 1};
    cout << robDP(nums) << endl;           // 4
    cout << robDPOptimized(nums) << endl;  // 4

    return 0;
}
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
from typing import List


# DP
def wiggleMaxLengthDP(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)

    up = [0 for _ in range(len(nums))]
    down = [0 for _ in range(len(nums))]

    up[0], down[0] = 1, 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] < nums[i - 1]:
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]
        else:
            up[i] = up[i - 1]
            down[i] = down[i - 1]

    return max(up[-1], down[-1])


# Greedy
def wiggleMaxLengthGreedy(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)

    prev_diff = nums[1] - nums[0]
    count = 2 if prev_diff != 0 else 1

    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
            count += 1
            prev_diff = diff

    return count


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    DP       |      O(n)       |     O(n)     |
# |  Greedy     |      O(n)       |     O(1)     |
# |-------------|-----------------|--------------|

nums = [1, 7, 4, 9, 2, 5]
print(wiggleMaxLengthDP(nums))  # 6
print(wiggleMaxLengthGreedy(nums))  # 6

```

## 343. Integer Break

-   [LeetCode](https://leetcode.com/problems/integer-break/) | [LeetCode CH](https://leetcode.cn/problems/integer-break/) (Medium)

-   Tags: math, dynamic programming
-   Return the maximum product of the integer after breaking it into at least two positive integers.
-   `dp[i]` stores the maximum product of the integer `i`.
-   Formula: `dp[i] = max(dp[i - j] * j, (i - j) * j)`
-   Time Complexity: O(n^2)
-   Space Complexity: O(n)

| dp        | 3       | 4       | 5       | 6       | 7        | 8        |
|:---------:|:-------:|:-------:|:-------:|:-------:|:--------:|:--------:|
| 2         | 2*1=2   | 2*2=4   | 2*3=6   | 2*4=8   | 2*5=10   | 2*6=12   |
| dp[2]=1   | 1*1=1   | 1*2=2   | 1*3=3   | 1*4=4   | 1*5=5    | 1*6=6    |
| 3         |         | 3*1=3   | 3*2=6   | 3*3=9   | 3*4=12   | 3*5=15   |
| dp[3]=2   |         | 2*1=2   | 2*2=4   | 2*3=6   | 2*4=8    | 2*5=10   |
| 4         |         |         | 4*1=4   | 4*2=8   | 4*3=12   | 4*4=16   |
| dp[4]=4   |         |         | 4*1=4   | 4*2=8   | 4*3=12   | 4*4=16   |
| 5         |         |         |         | 5*1=5   | 5*2=10   | 5*3=15   |
| dp[5]=6   |         |         |         | 6*1=6   | 6*2=12   | 6*3=18   |
| 6         |         |         |         |         | 6*1=6    | 6*2=12   |
| dp[6]=9   |         |         |         |         | 9*1=9    | 9*2=18   |
| 7         |         |         |         |         |          | 7*1=7    |
| dp[7]=12  |         |         |         |         |          | 12*1=12  |
| `dp[n]`   | 2       | 4       | 6       | 9       | 12       | 18       |

```python title="343. Integer Break - Python Solution"
def integerBreak(n: int) -> int:
    dp = [0 for _ in range(n + 1)]
    dp[2] = 1

    for i in range(3, n + 1):
        for j in range(2, i):
            dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)

    return dp[n]


if __name__ == "__main__":
    print(integerBreak(8))  # 18

```

## 1025. Divisor Game

-   [LeetCode](https://leetcode.com/problems/divisor-game/) | [LeetCode CH](https://leetcode.cn/problems/divisor-game/) (Easy)

-   Tags: math, dynamic programming, brainteaser, game theory
-   Return `True` if Alice wins the game, assuming both players play optimally.
-   `dp[n]` stores the result of the game when the number is `n`.
-   Initialize `dp[1] = False`.

```python title="1025. Divisor Game - Python Solution"
# DP
def divisorGameDP(n: int) -> bool:
    if n <= 1:
        return False

    dp = [False for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0 and not dp[i - j]:
                dp[i] = True
                break

    return dp[n]


# Math
def divisorGameDPMath(n: int) -> bool:
    return n % 2 == 0


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |  DP         |      O(n^2)     |    O(n)      |
# |  Math       |      O(1)       |    O(1)      |
# |-------------|-----------------|--------------|

n = 2
print(divisorGameDP(n))  # True
print(divisorGameDPMath(n))  # True

```

