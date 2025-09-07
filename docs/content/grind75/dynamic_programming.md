---
comments: True
---

# Dynamic Programming

## Table of Contents

- [x] [70. Climbing Stairs](https://leetcode.cn/problems/climbing-stairs/) (Easy)
- [x] [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) (Medium)
- [x] [322. Coin Change](https://leetcode.cn/problems/coin-change/) (Medium)
- [x] [416. Partition Equal Subset Sum](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)
- [x] [62. Unique Paths](https://leetcode.cn/problems/unique-paths/) (Medium)

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

## 53. Maximum Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray/) (Medium)

-   Tags: array, divide and conquer, dynamic programming
```python title="53. Maximum Subarray - Python Solution"
from typing import List


# DP Kadane
def maxSubArrayDP(nums: List[int]) -> int:
    dp = [0 for _ in range(len(nums))]

    dp[0] = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(
            dp[i - 1] + nums[i],  # continue the previous subarray
            nums[i],  # start a new subarray
        )
        maxSum = max(maxSum, dp[i])

    return maxSum


# Greedy
def maxSubArrayGreedy(nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = 0

    for num in nums:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)

    return max_sum


# Prefix Sum
def maxSubArrayPrefixSum(nums: List[int]) -> int:
    prefix_sum = 0
    prefix_sum_min = 0
    res = float("-inf")

    for num in nums:
        prefix_sum += num
        res = max(res, prefix_sum - prefix_sum_min)
        prefix_sum_min = min(prefix_sum_min, prefix_sum)

    return res


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArrayDP(nums))  # 6
print(maxSubArrayGreedy(nums))  # 6
print(maxSubArrayPrefixSum(nums))  # 6

```

## 322. Coin Change

-   [LeetCode](https://leetcode.com/problems/coin-change/) | [LeetCode CH](https://leetcode.cn/problems/coin-change/) (Medium)

-   Tags: array, dynamic programming, breadth first search
```python title="322. Coin Change - Python Solution"
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float("inf") for _ in range(amount + 1)]

    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return dp[amount] if dp[amount] != float("inf") else -1


coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # 3

```

## 416. Partition Equal Subset Sum

-   [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) | [LeetCode CH](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)

-   Tags: array, dynamic programming
```python title="416. Partition Equal Subset Sum - Python Solution"
from functools import cache
from typing import List

from leetpattern.utils import knapsack01


# Memoization
def canPartitionMemoization(nums: List[int]) -> bool:
    total = sum(nums)
    n = len(nums)

    if total % 2 == 1 or n <= 1:
        return False

    @cache
    def dfs(i, j):
        if i < 0:
            return j == 0
        return j >= nums[i] and dfs(i - 1, j - nums[i]) or dfs(i - 1, j)

    return dfs(n - 1, total // 2)


# DP - Knapsack 01
def canPartitionTemplate(nums: List[int]) -> bool:
    total = sum(nums)

    if total % 2 == 1 or len(nums) < 2:
        return False

    target = total // 2

    return knapsack01(nums, nums, target) == target


# DP - Knapsack 01
def canPartition(nums: List[int]) -> bool:
    total = sum(nums)

    if total % 2 == 1 or len(nums) < 2:
        return False

    target = total // 2

    dp = [0 for _ in range(target + 1)]

    for i in range(len(nums)):
        for j in range(target, nums[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

    return dp[target] == target


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(canPartitionTemplate(nums))  # True
    print(canPartition(nums))  # True
    print(canPartitionMemoization(nums))  # True

```

## 62. Unique Paths

-   [LeetCode](https://leetcode.com/problems/unique-paths/) | [LeetCode CH](https://leetcode.cn/problems/unique-paths/) (Medium)

-   Tags: math, dynamic programming, combinatorics
-   Count the number of unique paths to reach the bottom-right corner of a `m x n` grid.

![62](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```python title="62. Unique Paths - Python Solution"
# DP - 2D
def uniquePaths(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1

    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


print(uniquePaths(m=3, n=7))  # 28
# [[1, 1, 1,  1,  1,  1,  1],
#  [1, 2, 3,  4,  5,  6,  7],
#  [1, 3, 6, 10, 15, 21, 28]]

```

```cpp title="62. Unique Paths - C++ Solution"
#include <iostream>
#include <vector>
using namespace std;

int uniquePaths(int m, int n) {
    vector dp(m, vector<int>(n, 1));

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }

    return dp[m - 1][n - 1];
}

int main() {
    int m = 3, n = 7;
    cout << uniquePaths(m, n) << endl;  // 28
    return 0;
}
```
