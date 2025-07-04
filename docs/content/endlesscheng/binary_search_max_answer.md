---
comments: True
---

# Binary Search Max Answer

## Table of Contents

- [x] [275. H-Index II](https://leetcode.cn/problems/h-index-ii/) (Medium)
- [x] [2226. Maximum Candies Allocated to K Children](https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/) (Medium)
- [ ] [2982. Find Longest Special Substring That Occurs Thrice II](https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/) (Medium)
- [x] [2576. Find the Maximum Number of Marked Indices](https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/) (Medium)
- [ ] [1898. Maximum Number of Removable Characters](https://leetcode.cn/problems/maximum-number-of-removable-characters/) (Medium)
- [ ] [1802. Maximum Value at a Given Index in a Bounded Array](https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/) (Medium)
- [ ] [1642. Furthest Building You Can Reach](https://leetcode.cn/problems/furthest-building-you-can-reach/) (Medium)
- [ ] [2861. Maximum Number of Alloys](https://leetcode.cn/problems/maximum-number-of-alloys/) (Medium)
- [ ] [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/) (Medium)
- [ ] [2141. Maximum Running Time of N Computers](https://leetcode.cn/problems/maximum-running-time-of-n-computers/) (Hard)
- [ ] [2258. Escape the Spreading Fire](https://leetcode.cn/problems/escape-the-spreading-fire/) (Hard)
- [ ] [2071. Maximum Number of Tasks You Can Assign](https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/) (Hard)
- [ ] [1618. Maximum Font to Fit a Sentence in a Screen](https://leetcode.cn/problems/maximum-font-to-fit-a-sentence-in-a-screen/) (Medium) 👑
- [ ] [1891. Cutting Ribbons](https://leetcode.cn/problems/cutting-ribbons/) (Medium) 👑
- [ ] [2137. Pour Water Between Buckets to Make Water Levels Equal](https://leetcode.cn/problems/pour-water-between-buckets-to-make-water-levels-equal/) (Medium) 👑
- [ ] [644. Maximum Average Subarray II](https://leetcode.cn/problems/maximum-average-subarray-ii/) (Hard) 👑

## 275. H-Index II

-   [LeetCode](https://leetcode.com/problems/h-index-ii/) | [LeetCode CH](https://leetcode.cn/problems/h-index-ii/) (Medium)

-   Tags: array, binary search
- Hint: logarithmic time -- binary search


```python title="275. H-Index II - Python Solution"
from typing import List


# Binary Search Max Answer
def hIndex(citations: List[int]) -> int:
    n = len(citations)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if citations[mid] >= n - mid:
            right = mid - 1
        else:
            left = mid + 1

    return n - left


if __name__ == "__main__":
    citations = [0, 1, 3, 5, 6]
    assert hIndex(citations) == 3

```

## 2226. Maximum Candies Allocated to K Children

-   [LeetCode](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/) | [LeetCode CH](https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/) (Medium)

-   Tags: array, binary search

```python title="2226. Maximum Candies Allocated to K Children - Python Solution"
from typing import List


# Binary Search Max Answer
def maximumCandies(candies: List[int], k: int) -> int:
    def check(low):
        return sum(c // low for c in candies) >= k

    left, right = 0, max(candies) + 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid
        else:
            right = mid

    return left


# Binary Search Max Answer - Optimized
def maximumCandiesOptimized(candies: List[int], k: int) -> int:
    def check(low):
        return sum(c // low for c in candies) >= k

    # Use the minimum of max(candies) and sum(candies) // k to limit the search space
    left, right = 0, min(max(candies), sum(candies) // k) + 1

    while left + 1 < right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid
        else:
            right = mid

    return left


if __name__ == "__main__":
    candies = [5, 8, 6]
    k = 3
    assert maximumCandies(candies, k) == 5
    assert maximumCandiesOptimized(candies, k) == 5

```

## 2982. Find Longest Special Substring That Occurs Thrice II

-   [LeetCode](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/) (Medium)

-   Tags: hash table, string, binary search, sliding window, counting
## 2576. Find the Maximum Number of Marked Indices

-   [LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/) | [LeetCode CH](https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/) (Medium)

-   Tags: array, two pointers, binary search, greedy, sorting

```python title="2576. Find the Maximum Number of Marked Indices - Python Solution"
from typing import List


# Fast Slow Pointers
def maxNumOfMarkedIndices(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    slow, fast = 0, n // 2
    count = 0

    while slow < n // 2 and fast < n:
        if nums[fast] >= 2 * nums[slow]:
            count += 2
            slow += 1
        fast += 1

    return count


nums = [3, 5, 2, 4]
print(maxNumOfMarkedIndices(nums))  # 2

```

## 1898. Maximum Number of Removable Characters

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-removable-characters/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-removable-characters/) (Medium)

-   Tags: array, two pointers, string, binary search
## 1802. Maximum Value at a Given Index in a Bounded Array

-   [LeetCode](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/) | [LeetCode CH](https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/) (Medium)

-   Tags: binary search, greedy
## 1642. Furthest Building You Can Reach

-   [LeetCode](https://leetcode.com/problems/furthest-building-you-can-reach/) | [LeetCode CH](https://leetcode.cn/problems/furthest-building-you-can-reach/) (Medium)

-   Tags: array, greedy, heap priority queue
## 2861. Maximum Number of Alloys

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-alloys/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-alloys/) (Medium)

-   Tags: array, binary search
## 3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K

-   [LeetCode](https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/) (Medium)

-   Tags: binary search, dynamic programming, bit manipulation
## 2141. Maximum Running Time of N Computers

-   [LeetCode](https://leetcode.com/problems/maximum-running-time-of-n-computers/) | [LeetCode CH](https://leetcode.cn/problems/maximum-running-time-of-n-computers/) (Hard)

-   Tags: array, binary search, greedy, sorting
## 2258. Escape the Spreading Fire

-   [LeetCode](https://leetcode.com/problems/escape-the-spreading-fire/) | [LeetCode CH](https://leetcode.cn/problems/escape-the-spreading-fire/) (Hard)

-   Tags: array, binary search, breadth first search, matrix
## 2071. Maximum Number of Tasks You Can Assign

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/) (Hard)

-   Tags: array, binary search, greedy, queue, sorting, monotonic queue
## 1618. Maximum Font to Fit a Sentence in a Screen

-   [LeetCode](https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/) | [LeetCode CH](https://leetcode.cn/problems/maximum-font-to-fit-a-sentence-in-a-screen/) (Medium)

-   Tags: array, string, binary search, interactive
## 1891. Cutting Ribbons

-   [LeetCode](https://leetcode.com/problems/cutting-ribbons/) | [LeetCode CH](https://leetcode.cn/problems/cutting-ribbons/) (Medium)

-   Tags: array, binary search
## 2137. Pour Water Between Buckets to Make Water Levels Equal

-   [LeetCode](https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/) | [LeetCode CH](https://leetcode.cn/problems/pour-water-between-buckets-to-make-water-levels-equal/) (Medium)

-   Tags: array, binary search
## 644. Maximum Average Subarray II

-   [LeetCode](https://leetcode.com/problems/maximum-average-subarray-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-average-subarray-ii/) (Hard)

-   Tags: array, binary search, prefix sum
