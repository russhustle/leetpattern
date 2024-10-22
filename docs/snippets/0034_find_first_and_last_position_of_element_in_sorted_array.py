from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:

    def binarySearch(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    left = binarySearch(nums, target)
    right = binarySearch(nums, target + 1) - 1

    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    return [left, right]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))
