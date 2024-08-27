from typing import List


# 1. [left, right]
def search1(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 2. [left, right)
def search2(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search1(nums, target))  # 4
print(search2(nums, target))  # 4
