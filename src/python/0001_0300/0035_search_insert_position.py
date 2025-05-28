"""
-   Return the index of the target if it is found. If not, return the index where it would be if it were inserted in order.
"""

from typing import List


# Binary Search
def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return left


nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # 2
