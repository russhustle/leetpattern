---
comments: True
---

# DP 01 Knapsack

## Table of Contents

- [x] [416. Partition Equal Subset Sum](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)
- [x] [474. Ones and Zeroes](https://leetcode.cn/problems/ones-and-zeroes/) (Medium)
- [x] [494. Target Sum](https://leetcode.cn/problems/target-sum/) (Medium)
- [x] [1046. Last Stone Weight](https://leetcode.cn/problems/last-stone-weight/) (Easy)
- [x] [1049. Last Stone Weight II](https://leetcode.cn/problems/last-stone-weight-ii/) (Medium)

## 416. Partition Equal Subset Sum

-   [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) | [LeetCode CH](https://leetcode.cn/problems/partition-equal-subset-sum/) (Medium)

-   Tags: array, dynamic programming

```python title="416. Partition Equal Subset Sum - Python Solution"
from typing import List

from template import knapsack01
from functools import cache


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

## 1046. Last Stone Weight

-   [LeetCode](https://leetcode.com/problems/last-stone-weight/) | [LeetCode CH](https://leetcode.cn/problems/last-stone-weight/) (Easy)

-   Tags: array, heap priority queue

```python title="1046. Last Stone Weight - Python Solution"
import heapq
from typing import List


# Heap
def lastStoneWeightHeap(stones: List[int]) -> int:
    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        s1 = heapq.heappop(heap)
        s2 = heapq.heappop(heap)

        if s1 != s2:
            heapq.heappush(heap, s1 - s2)

    return -heap[0] if heap else 0


# 0/1 Knapsack
def lastStoneWeightKnapsack(stones: List[int]) -> int:
    total = sum(stones)
    target = total // 2

    dp = [0 for _ in range(target + 1)]

    for i in stones:
        for j in range(target, i - 1, -1):
            dp[j] = max(dp[j], dp[j - i] + i)

    return total - 2 * dp[target]


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    Heap     |   O(n log n)    |     O(n)     |
# |  Knapsack   |      O(n)       |     O(n)     |
# |-------------|-----------------|--------------|


stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeightHeap(stones))  # 1
print(lastStoneWeightKnapsack(stones))  # 1

```

```cpp title="1046. Last Stone Weight - C++ Solution"
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int lastStoneWeight(vector<int> &stones)
{
    priority_queue<int> maxHeap(stones.begin(), stones.end());

    while (maxHeap.size() >= 1)
    {
        int first = maxHeap.top();
        maxHeap.pop();
        int second = maxHeap.top();
        maxHeap.pop();

        if (first != second)
        {
            maxHeap.push(first - second);
        }
    }

    return maxHeap.empty() ? 0 : maxHeap.top();
}

int main()
{
    vector<int> stones = {2, 7, 4, 1, 8, 1};
    cout << lastStoneWeight(stones) << endl; // 1
    return 0;
}

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
