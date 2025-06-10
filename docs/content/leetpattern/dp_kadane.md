---
comments: True
---

# DP Kadane

## Table of Contents

- [x] [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) (Medium)
- [x] [918. Maximum Sum Circular Subarray](https://leetcode.cn/problems/maximum-sum-circular-subarray/) (Medium)
- [x] [152. Maximum Product Subarray](https://leetcode.cn/problems/maximum-product-subarray/) (Medium)
- [x] [978. Longest Turbulent Subarray](https://leetcode.cn/problems/longest-turbulent-subarray/) (Medium)
- [x] [1186. Maximum Subarray Sum with One Deletion](https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/) (Medium)

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

## 978. Longest Turbulent Subarray

-   [LeetCode](https://leetcode.com/problems/longest-turbulent-subarray/) | [LeetCode CH](https://leetcode.cn/problems/longest-turbulent-subarray/) (Medium)

-   Tags: array, dynamic programming, sliding window

```python title="978. Longest Turbulent Subarray - Python Solution"
from typing import List


# DP - Kadane
def maxTurbulenceSize(arr: List[int]) -> int:
    n = len(arr)
    up = [1 for _ in range(n)]
    down = [1 for _ in range(n)]
    maxLen = 1

    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            up[i] = down[i - 1] + 1
            down[i] = 1
        elif arr[i - 1] > arr[i]:
            down[i] = up[i - 1] + 1
            up[i] = 1
        else:
            up[i] = 1
            down[i] = 1

        maxLen = max(maxLen, up[i], down[i])

    return maxLen


arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print(maxTurbulenceSize(arr))  # 5

```

## 1186. Maximum Subarray Sum with One Deletion

-   [LeetCode](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) | [LeetCode CH](https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/) (Medium)

-   Tags: array, dynamic programming
- [灵神：教你一步步思考动态规划 - 从记忆化搜索到递推](https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/solutions/2321829/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-hzz6))


```python title="1186. Maximum Subarray Sum with One Deletion - Python Solution"
from functools import cache
from math import inf
from typing import List


# DP - Kadane
def maximumSum(arr: List[int]) -> int:
    dp0 = arr[0]
    dp1 = 0
    res = dp0

    for i in range(1, len(arr)):
        dp1 = max(dp1 + arr[i], dp0)  # delete previous element or not
        dp0 = max(dp0, 0) + arr[i]  # delete current element or not
        res = max(res, dp0, dp1)  # update result

    return res


# DP - Memoization
def maximumSumMemo(arr: List[int]) -> int:
    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0:
            return -inf
        if j == 0:
            return max(dfs(i - 1, 0), 0) + arr[i]
        return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))

    return max(max(dfs(i, 0), dfs(i, 1)) for i in range(len(arr)))


if __name__ == "__main__":
    arr = [1, -2, 0, 3]
    assert maximumSum(arr) == 4
    assert maximumSumMemo(arr) == 4

```
