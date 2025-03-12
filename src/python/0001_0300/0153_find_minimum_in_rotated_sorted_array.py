from typing import List


# Binary Search
def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[right]


nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))  # 0
