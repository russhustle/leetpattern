---
comments: True
---

# Sliding Window Variable Subarrays Shorter

## Table of Contents

- [x] [713. Subarray Product Less Than K](https://leetcode.cn/problems/subarray-product-less-than-k/) (Medium)
- [ ] [3258. Count Substrings That Satisfy K-Constraint I](https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/) (Easy)
- [ ] [2302. Count Subarrays With Score Less Than K](https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/) (Hard)
- [ ] [2762. Continuous Subarrays](https://leetcode.cn/problems/continuous-subarrays/) (Medium)
- [ ] [3134. Find the Median of the Uniqueness Array](https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/) (Hard)
- [ ] [3261. Count Substrings That Satisfy K-Constraint II](https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/) (Hard)
- [ ] [2743. Count Substrings Without Repeating Character](https://leetcode.cn/problems/count-substrings-without-repeating-character/) (Medium) 👑

## 713. Subarray Product Less Than K

-   [LeetCode](https://leetcode.com/problems/subarray-product-less-than-k/) | [LeetCode CH](https://leetcode.cn/problems/subarray-product-less-than-k/) (Medium)

-   Tags: array, binary search, sliding window, prefix sum

```python title="713. Subarray Product Less Than K - Python Solution"
from typing import List


# Sliding window - Fixed
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    left = 0
    product = 1
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        count += right - left + 1

    return count


nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))  # 8

```

## 3258. Count Substrings That Satisfy K-Constraint I

-   [LeetCode](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/) | [LeetCode CH](https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/) (Easy)

-   Tags: string, sliding window

## 2302. Count Subarrays With Score Less Than K

-   [LeetCode](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/) | [LeetCode CH](https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/) (Hard)

-   Tags: array, binary search, sliding window, prefix sum

## 2762. Continuous Subarrays

-   [LeetCode](https://leetcode.com/problems/continuous-subarrays/) | [LeetCode CH](https://leetcode.cn/problems/continuous-subarrays/) (Medium)

-   Tags: array, queue, sliding window, heap priority queue, ordered set, monotonic queue

## 3134. Find the Median of the Uniqueness Array

-   [LeetCode](https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/) | [LeetCode CH](https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/) (Hard)

-   Tags: array, hash table, binary search, sliding window

## 3261. Count Substrings That Satisfy K-Constraint II

-   [LeetCode](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/) | [LeetCode CH](https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/) (Hard)

-   Tags: array, string, binary search, sliding window, prefix sum

## 2743. Count Substrings Without Repeating Character

-   [LeetCode](https://leetcode.com/problems/count-substrings-without-repeating-character/) | [LeetCode CH](https://leetcode.cn/problems/count-substrings-without-repeating-character/) (Medium)

-   Tags: hash table, string, sliding window
