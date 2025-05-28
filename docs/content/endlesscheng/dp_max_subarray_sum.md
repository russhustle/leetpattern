---
comments: True
---

# DP Max Subarray Sum

## Table of Contents

- [x] [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) (Medium)
- [ ] [2606. Find the Substring With Maximum Cost](https://leetcode.cn/problems/find-the-substring-with-maximum-cost/) (Medium)
- [ ] [1749. Maximum Absolute Sum of Any Subarray](https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/) (Medium)
- [ ] [1191. K-Concatenation Maximum Sum](https://leetcode.cn/problems/k-concatenation-maximum-sum/) (Medium)
- [x] [918. Maximum Sum Circular Subarray](https://leetcode.cn/problems/maximum-sum-circular-subarray/) (Medium)
- [ ] [2321. Maximum Score Of Spliced Array](https://leetcode.cn/problems/maximum-score-of-spliced-array/) (Hard)
- [x] [152. Maximum Product Subarray](https://leetcode.cn/problems/maximum-product-subarray/) (Medium)

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

## 2606. Find the Substring With Maximum Cost

-   [LeetCode](https://leetcode.com/problems/find-the-substring-with-maximum-cost/) | [LeetCode CH](https://leetcode.cn/problems/find-the-substring-with-maximum-cost/) (Medium)

-   Tags: array, hash table, string, dynamic programming
## 1749. Maximum Absolute Sum of Any Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/) (Medium)

-   Tags: array, dynamic programming
## 1191. K-Concatenation Maximum Sum

-   [LeetCode](https://leetcode.com/problems/k-concatenation-maximum-sum/) | [LeetCode CH](https://leetcode.cn/problems/k-concatenation-maximum-sum/) (Medium)

-   Tags: array, dynamic programming
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

## 2321. Maximum Score Of Spliced Array

-   [LeetCode](https://leetcode.com/problems/maximum-score-of-spliced-array/) | [LeetCode CH](https://leetcode.cn/problems/maximum-score-of-spliced-array/) (Hard)

-   Tags: array, dynamic programming
## 152. Maximum Product Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-product-subarray/) (Medium)

-   Tags: array, dynamic programming

```python title="152. Maximum Product Subarray - Python Solution"
from typing import List


# DP - Kadane
def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    dp_max = [0 for _ in range(n)]
    dp_min = [0 for _ in range(n)]

    dp_max[0] = nums[0]
    dp_min[0] = nums[0]
    max_product = nums[0]

    for i in range(1, n):
        dp_max[i] = max(
            nums[i],
            nums[i] * dp_max[i - 1],
            nums[i] * dp_min[i - 1],
        )
        dp_min[i] = min(
            nums[i],
            nums[i] * dp_max[i - 1],
            nums[i] * dp_min[i - 1],
        )

        max_product = max(max_product, dp_max[i])

    return max_product


nums = [2, 3, -2, 4]
print(maxProduct(nums))  # 6

```
