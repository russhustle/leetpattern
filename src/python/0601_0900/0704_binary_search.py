"""
- Implement binary search algorithm.
"""

from typing import List


# Binary Search [left, right]
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1


# Binary Search [left, right)
def search_half_open(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            return mid

    return -1


# Binary Search (left, right)
def search_open_interval(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)

    while left + 1 < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            return mid

    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert search(nums, target) == 4
    assert search_half_open(nums, target) == 4
    assert search_open_interval(nums, target) == 4
