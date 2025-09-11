"""
-   Move all zeroes to the end of the array while maintaining the relative order of the non-zero elements.
"""

from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    fast, slow = 0, 0

    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # [1, 3, 12, 0, 0]
