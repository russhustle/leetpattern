from bisect import bisect_left
from typing import List


# Binary Search
def searchRangeBS(nums: List[int], target: int) -> List[int]:
    def bisect_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    left = bisect_left(nums, target)
    right = bisect_left(nums, target + 1) - 1

    if left <= right:
        return [left, right]

    return [-1, -1]


# Bisect
def searchRangeBSBisect(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]

    left = bisect_left(nums, target)
    right = bisect_left(nums, target + 1) - 1

    return [left, right] if left <= right else [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRangeBS(nums, target))  # [3, 4]
print(searchRangeBSBisect(nums, target))  # [3, 4]
