---
comments: True
---

# Kadane Algorithm

## Table of Contents

- [x] [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) (Medium)
- [x] [918. Maximum Sum Circular Subarray](https://leetcode.cn/problems/maximum-sum-circular-subarray/) (Medium)

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

## 918. Maximum Sum Circular Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-sum-circular-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-sum-circular-subarray/) (Medium)

-   Tags: array, divide and conquer, dynamic programming, queue, monotonic queue

```python title="918. Maximum Sum Circular Subarray - Python Solution"
from collections import deque
from typing import List


# DP - Kadane
def maxSubarraySumCircularKadane(nums: List[int]) -> int:
    max_sum = min_sum = nums[0]
    max_cur = min_cur = 0
    total = 0

    for num in nums:
        max_cur = max(max_cur + num, num)
        min_cur = min(min_cur + num, num)
        total += num

        max_sum = max(max_sum, max_cur)
        min_sum = min(min_sum, min_cur)

    return max(max_sum, total - min_sum) if max_sum > 0 else max_sum


# Monotonic Queue
def maxSubarraySumCircularMQ(nums: List[int]) -> int:
    n = len(nums)
    prefix_sum = [0] * (2 * n + 1)

    for i in range(1, 2 * n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[(i - 1) % n]

    q = deque([0])
    max_sum = float("-inf")

    for i in range(1, 2 * n + 1):
        if q[0] < i - n:
            q.popleft()

        max_sum = max(max_sum, prefix_sum[i] - prefix_sum[q[0]])

        while q and prefix_sum[q[-1]] >= prefix_sum[i]:
            q.pop()

        q.append(i)

    return max_sum


nums = [1, -2, 3, -2]
print(maxSubarraySumCircularKadane(nums))  # 3
print(maxSubarraySumCircularMQ(nums))  # 3

```
