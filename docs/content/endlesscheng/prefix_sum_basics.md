---
comments: True
---

# Prefix Sum Basics

## Table of Contents

- [x] [303. Range Sum Query - Immutable](https://leetcode.cn/problems/range-sum-query-immutable/) (Easy)
- [ ] [3427. Sum of Variable Length Subarrays](https://leetcode.cn/problems/sum-of-variable-length-subarrays/) (Easy)
- [ ] [2559. Count Vowel Strings in Ranges](https://leetcode.cn/problems/count-vowel-strings-in-ranges/) (Medium)
- [ ] [3152. Special Array II](https://leetcode.cn/problems/special-array-ii/) (Medium)
- [ ] [1749. Maximum Absolute Sum of Any Subarray](https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/) (Medium)
- [ ] [2389. Longest Subsequence With Limited Sum](https://leetcode.cn/problems/longest-subsequence-with-limited-sum/) (Easy)
- [ ] [3361. Shift Distance Between Two Strings](https://leetcode.cn/problems/shift-distance-between-two-strings/) (Medium)
- [ ] [2055. Plates Between Candles](https://leetcode.cn/problems/plates-between-candles/) (Medium)
- [ ] [1744. Can You Eat Your Favorite Candy on Your Favorite Day?](https://leetcode.cn/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/) (Medium)
- [x] [53. Maximum Subarray](https://leetcode.cn/problems/maximum-subarray/) (Medium)
- [ ] [1523. Count Odd Numbers in an Interval Range](https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/) (Easy)

## 303. Range Sum Query - Immutable

-   [LeetCode](https://leetcode.com/problems/range-sum-query-immutable/) | [LeetCode CH](https://leetcode.cn/problems/range-sum-query-immutable/) (Easy)

-   Tags: array, design, prefix sum

```python title="303. Range Sum Query - Immutable - Python Solution"
from typing import List


# Prefix Sum
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.ps = [0 for _ in range(n + 1)]  # prefix sum
        for i in range(1, n + 1):
            self.ps[i] = self.ps[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right + 1] - self.ps[left]


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
assert obj.sumRange(0, 2) == 1
assert obj.sumRange(2, 5) == -1
assert obj.sumRange(0, 5) == -3
print("PASSED")

```

## 3427. Sum of Variable Length Subarrays

-   [LeetCode](https://leetcode.com/problems/sum-of-variable-length-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/sum-of-variable-length-subarrays/) (Easy)

-   Tags: array, prefix sum

## 2559. Count Vowel Strings in Ranges

-   [LeetCode](https://leetcode.com/problems/count-vowel-strings-in-ranges/) | [LeetCode CH](https://leetcode.cn/problems/count-vowel-strings-in-ranges/) (Medium)

-   Tags: array, string, prefix sum

## 3152. Special Array II

-   [LeetCode](https://leetcode.com/problems/special-array-ii/) | [LeetCode CH](https://leetcode.cn/problems/special-array-ii/) (Medium)

-   Tags: array, binary search, prefix sum

## 1749. Maximum Absolute Sum of Any Subarray

-   [LeetCode](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) | [LeetCode CH](https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/) (Medium)

-   Tags: array, dynamic programming

## 2389. Longest Subsequence With Limited Sum

-   [LeetCode](https://leetcode.com/problems/longest-subsequence-with-limited-sum/) | [LeetCode CH](https://leetcode.cn/problems/longest-subsequence-with-limited-sum/) (Easy)

-   Tags: array, binary search, greedy, sorting, prefix sum

## 3361. Shift Distance Between Two Strings

-   [LeetCode](https://leetcode.com/problems/shift-distance-between-two-strings/) | [LeetCode CH](https://leetcode.cn/problems/shift-distance-between-two-strings/) (Medium)

-   Tags: array, string, prefix sum

## 2055. Plates Between Candles

-   [LeetCode](https://leetcode.com/problems/plates-between-candles/) | [LeetCode CH](https://leetcode.cn/problems/plates-between-candles/) (Medium)

-   Tags: array, string, binary search, prefix sum

## 1744. Can You Eat Your Favorite Candy on Your Favorite Day?

-   [LeetCode](https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/) | [LeetCode CH](https://leetcode.cn/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/) (Medium)

-   Tags: array, prefix sum

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

## 1523. Count Odd Numbers in an Interval Range

-   [LeetCode](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) | [LeetCode CH](https://leetcode.cn/problems/count-odd-numbers-in-an-interval-range/) (Easy)

-   Tags: math
