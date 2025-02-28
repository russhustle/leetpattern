from bisect import bisect_left, bisect_right
from typing import List


# Binary Search
def maximumCount(nums: List[int]) -> int:
    pos = bisect_left(nums, 0)
    neg = len(nums) - bisect_right(nums, 0)

    return max(pos, neg)


nums = [-2, -1, -1, 1, 2, 3]
print(maximumCount(nums))  # 3
