---
comments: True
---

# DP 0-1 Knapsack

## Table of Contents

- [ ] [2915. Length of the Longest Subsequence That Sums to Target](https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/) (Medium)
- [x] [416. Partition Equal Subset Sum](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)
- [x] [494. Target Sum](https://leetcode.cn/problems/target-sum/) (Medium)
- [ ] [2787. Ways to Express an Integer as Sum of Powers](https://leetcode.cn/problems/ways-to-express-an-integer-as-sum-of-powers/) (Medium)
- [ ] [3180. Maximum Total Reward Using Operations I](https://leetcode.cn/problems/maximum-total-reward-using-operations-i/) (Medium)
- [x] [474. Ones and Zeroes](https://leetcode.cn/problems/ones-and-zeroes/) (Medium)
- [x] [1049. Last Stone Weight II](https://leetcode.cn/problems/last-stone-weight-ii/) (Medium)
- [ ] [1774. Closest Dessert Cost](https://leetcode.cn/problems/closest-dessert-cost/) (Medium)
- [ ] [879. Profitable Schemes](https://leetcode.cn/problems/profitable-schemes/) (Hard)
- [ ] [3082. Find the Sum of the Power of All Subsequences](https://leetcode.cn/problems/find-the-sum-of-the-power-of-all-subsequences/) (Hard)
- [ ] [956. Tallest Billboard](https://leetcode.cn/problems/tallest-billboard/) (Hard)
- [ ] [2518. Number of Great Partitions](https://leetcode.cn/problems/number-of-great-partitions/) (Hard)
- [ ] [2742. Painting the Walls](https://leetcode.cn/problems/painting-the-walls/) (Hard)
- [ ] [3287. Find the Maximum Sequence Value of Array](https://leetcode.cn/problems/find-the-maximum-sequence-value-of-array/) (Hard)
- [ ] [2291. Maximum Profit From Trading Stocks](https://leetcode.cn/problems/maximum-profit-from-trading-stocks/) (Medium) 👑
- [ ] [2431. Maximize Total Tastiness of Purchased Fruits](https://leetcode.cn/problems/maximize-total-tastiness-of-purchased-fruits/) (Medium) 👑

## 2915. Length of the Longest Subsequence That Sums to Target

-   [LeetCode](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/) | [LeetCode CH](https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/) (Medium)

-   Tags: array, dynamic programming
## 416. Partition Equal Subset Sum

-   [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) | [LeetCode CH](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)

-   Tags: array, dynamic programming

```python title="416. Partition Equal Subset Sum - Python Solution"
from functools import cache
from typing import List

from template import knapsack01


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

## 494. Target Sum

-   [LeetCode](https://leetcode.com/problems/target-sum/) | [LeetCode CH](https://leetcode.cn/problems/target-sum/) (Medium)

-   Tags: array, dynamic programming, backtracking

```python title="494. Target Sum - Python Solution"
from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:

    totalSum = sum(nums)

    if abs(target) > totalSum:
        return 0
    if (target + totalSum) % 2 == 1:
        return 0

    targetSum = (target + totalSum) // 2
    dp = [0] * (targetSum + 1)
    dp[0] = 1

    for i in range(len(nums)):
        for j in range(targetSum, nums[i] - 1, -1):
            dp[j] += dp[j - nums[i]]

    return dp[targetSum]


nums = [1, 1, 1, 1, 1]
target = 3
print(findTargetSumWays(nums, target))  # 5

```

## 2787. Ways to Express an Integer as Sum of Powers

-   [LeetCode](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/) | [LeetCode CH](https://leetcode.cn/problems/ways-to-express-an-integer-as-sum-of-powers/) (Medium)

-   Tags: dynamic programming
## 3180. Maximum Total Reward Using Operations I

-   [LeetCode](https://leetcode.com/problems/maximum-total-reward-using-operations-i/) | [LeetCode CH](https://leetcode.cn/problems/maximum-total-reward-using-operations-i/) (Medium)

-   Tags: array, dynamic programming
## 474. Ones and Zeroes

-   [LeetCode](https://leetcode.com/problems/ones-and-zeroes/) | [LeetCode CH](https://leetcode.cn/problems/ones-and-zeroes/) (Medium)

-   Tags: array, string, dynamic programming

```python title="474. Ones and Zeroes - Python Solution"
from typing import List


def findMaxForm(strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
        zerosNum = s.count("0")
        onesNum = len(s) - zerosNum

        for i in range(m, zerosNum - 1, -1):
            for j in range(n, onesNum - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zerosNum][j - onesNum] + 1)

    return dp[m][n]


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(findMaxForm(strs, m, n))  # 4

```

## 1049. Last Stone Weight II

-   [LeetCode](https://leetcode.com/problems/last-stone-weight-ii/) | [LeetCode CH](https://leetcode.cn/problems/last-stone-weight-ii/) (Medium)

-   Tags: array, dynamic programming

```python title="1049. Last Stone Weight II - Python Solution"
from typing import List


def lastStoneWeightII(stones: List[int]) -> int:
    target = sum(stones) // 2

    dp = [0 for _ in range(target + 1)]

    for i in range(len(stones)):
        for j in range(target, stones[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

    result = (sum(stones) - dp[target]) - dp[target]

    return result


stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeightII(stones))  # 1

```

## 1774. Closest Dessert Cost

-   [LeetCode](https://leetcode.com/problems/closest-dessert-cost/) | [LeetCode CH](https://leetcode.cn/problems/closest-dessert-cost/) (Medium)

-   Tags: array, dynamic programming, backtracking
## 879. Profitable Schemes

-   [LeetCode](https://leetcode.com/problems/profitable-schemes/) | [LeetCode CH](https://leetcode.cn/problems/profitable-schemes/) (Hard)

-   Tags: array, dynamic programming
## 3082. Find the Sum of the Power of All Subsequences

-   [LeetCode](https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/) | [LeetCode CH](https://leetcode.cn/problems/find-the-sum-of-the-power-of-all-subsequences/) (Hard)

-   Tags: array, dynamic programming
## 956. Tallest Billboard

-   [LeetCode](https://leetcode.com/problems/tallest-billboard/) | [LeetCode CH](https://leetcode.cn/problems/tallest-billboard/) (Hard)

-   Tags: array, dynamic programming
## 2518. Number of Great Partitions

-   [LeetCode](https://leetcode.com/problems/number-of-great-partitions/) | [LeetCode CH](https://leetcode.cn/problems/number-of-great-partitions/) (Hard)

-   Tags: array, dynamic programming
## 2742. Painting the Walls

-   [LeetCode](https://leetcode.com/problems/painting-the-walls/) | [LeetCode CH](https://leetcode.cn/problems/painting-the-walls/) (Hard)

-   Tags: array, dynamic programming
## 3287. Find the Maximum Sequence Value of Array

-   [LeetCode](https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/) | [LeetCode CH](https://leetcode.cn/problems/find-the-maximum-sequence-value-of-array/) (Hard)

-   Tags: array, dynamic programming, bit manipulation
## 2291. Maximum Profit From Trading Stocks

-   [LeetCode](https://leetcode.com/problems/maximum-profit-from-trading-stocks/) | [LeetCode CH](https://leetcode.cn/problems/maximum-profit-from-trading-stocks/) (Medium)

-   Tags: array, dynamic programming
## 2431. Maximize Total Tastiness of Purchased Fruits

-   [LeetCode](https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/) | [LeetCode CH](https://leetcode.cn/problems/maximize-total-tastiness-of-purchased-fruits/) (Medium)

-   Tags: array, dynamic programming
