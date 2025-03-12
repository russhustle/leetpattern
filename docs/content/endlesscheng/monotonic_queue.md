---
comments: True
---

# Monotonic Queue

- [x] [239. Sliding Window Maximum](https://leetcode.cn/problems/sliding-window-maximum/) (Hard)
- [ ] [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) (Medium)
- [ ] [2762. Continuous Subarrays](https://leetcode.cn/problems/continuous-subarrays/) (Medium)
- [x] [2398. Maximum Number of Robots Within Budget](https://leetcode.cn/problems/maximum-number-of-robots-within-budget/) (Hard)
- [x] [862. Shortest Subarray with Sum at Least K](https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/) (Hard)
- [ ] [1499. Max Value of Equation](https://leetcode.cn/problems/max-value-of-equation/) (Hard)
- [ ] [2071. Maximum Number of Tasks You Can Assign](https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/) (Hard)

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

## 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

-   [LeetCode](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | [LeetCode CH](https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) (Medium)

-   Tags: array, queue, sliding window, heap priority queue, ordered set, monotonic queue

## 2762. Continuous Subarrays

-   [LeetCode](https://leetcode.com/problems/continuous-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/continuous-subarrays/) (Medium)

-   Tags: array, queue, sliding window, heap priority queue, ordered set, monotonic queue

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

## 1499. Max Value of Equation

-   [LeetCode](https://leetcode.com/problems/max-value-of-equation/) | [LeetCode CH](https://leetcode.cn/problems/max-value-of-equation/) (Hard)

-   Tags: array, queue, sliding window, heap priority queue, monotonic queue

## 2071. Maximum Number of Tasks You Can Assign

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/) (Hard)

-   Tags: array, binary search, greedy, queue, sorting, monotonic queue
