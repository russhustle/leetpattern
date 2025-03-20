---
comments: True
---

# Queue Monotonic

## Table of Contents

- [x] [918. Maximum Sum Circular Subarray](https://leetcode.cn/problems/maximum-sum-circular-subarray/) (Medium)
- [x] [862. Shortest Subarray with Sum at Least K](https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/) (Hard)
- [x] [239. Sliding Window Maximum](https://leetcode.cn/problems/sliding-window-maximum/) (Hard)
- [x] [2398. Maximum Number of Robots Within Budget](https://leetcode.cn/problems/maximum-number-of-robots-within-budget/) (Hard)

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

## 862. Shortest Subarray with Sum at Least K

-   [LeetCode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | [LeetCode CH](https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/) (Hard)

-   Tags: array, binary search, queue, sliding window, heap priority queue, prefix sum, monotonic queue

```python title="862. Shortest Subarray with Sum at Least K - Python Solution"
from collections import deque
from typing import List


# Prefix Sum + Monotonic Queue
def shortestSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    ps = [0 for _ in range(n + 1)]

    for i in range(n):
        ps[i + 1] = ps[i] + nums[i]

    res = float("inf")
    q = deque()

    for i in range(n + 1):
        while q and ps[i] - ps[q[0]] >= k:
            res = min(res, i - q.popleft())
        while q and ps[i] <= ps[q[-1]]:
            q.pop()
        q.append(i)

    return res if res != float("inf") else -1


nums = [2, -1, 2]
k = 3
print(shortestSubarray(nums, k))  # 3

```

## 239. Sliding Window Maximum

-   [LeetCode](https://leetcode.com/problems/sliding-window-maximum/) | [LeetCode CH](https://leetcode.cn/problems/sliding-window-maximum/) (Hard)

-   Tags: array, queue, sliding window, heap priority queue, monotonic queue

```python title="239. Sliding Window Maximum - Python Solution"
from collections import deque
from typing import List


# Monotonic Queue
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque()
    res = []

    for i, num in enumerate(nums):
        if q and q[0] < i - k + 1:
            q.popleft()

        while q and nums[q[-1]] < num:
            q.pop()

        q.append(i)

        if i >= k - 1:
            res.append(nums[q[0]])

    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))  # [3, 3, 5, 5, 6, 7]

```

## 2398. Maximum Number of Robots Within Budget

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-robots-within-budget/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-robots-within-budget/) (Hard)

-   Tags: array, binary search, queue, sliding window, heap priority queue, prefix sum, monotonic queue

```python title="2398. Maximum Number of Robots Within Budget - Python Solution"
from collections import deque
from typing import List


# Monotonic Queue
def maximumRobots(
    chargeTimes: List[int], runningCosts: List[int], budget: int
) -> int:
    ans = sum_cost = left = 0
    q = deque()

    for right, (time, cost) in enumerate(zip(chargeTimes, runningCosts)):
        # 1. Add
        while q and time >= chargeTimes[q[-1]]:
            q.pop()
        q.append(right)
        sum_cost += cost

        # 2. Remove
        while q and chargeTimes[q[0]] + (right - left + 1) * sum_cost > budget:
            if q[0] == left:
                q.popleft()
            sum_cost -= runningCosts[left]
            left += 1

        # 3. Update
        ans = max(ans, right - left + 1)
    return ans


chargeTimes = [3, 6, 1, 3, 4]
runningCosts = [2, 1, 3, 4, 5]
budget = 25
print(maximumRobots(chargeTimes, runningCosts, budget))  # 3

```
