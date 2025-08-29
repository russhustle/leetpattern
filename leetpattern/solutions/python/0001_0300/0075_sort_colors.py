from copy import deepcopy
from typing import List


# Left Right Pointers
def sort_colors_lr_pointers(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    left = 0
    for right in range(n):
        if nums[right] == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    for right in range(left, n):
        if nums[right] == 1:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


# Three Pointers
def sort_colors_three_pointers(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left, right = 0, len(nums) - 1
    cur = 0

    while cur <= right:
        if nums[cur] == 0:
            nums[left], nums[cur] = nums[cur], nums[left]
            left += 1
            cur += 1
        elif nums[cur] == 2:
            nums[right], nums[cur] = nums[cur], nums[right]
            right -= 1
        else:
            cur += 1


nums = [2, 0, 2, 1, 1, 0]
nums1, nums2 = deepcopy(nums), deepcopy(nums)
sort_colors_lr_pointers(nums1)
print(nums1)  # [0, 0, 1, 1, 2, 2]
sort_colors_three_pointers(nums2)
print(nums2)  # [0, 0, 1, 1, 2, 2]
