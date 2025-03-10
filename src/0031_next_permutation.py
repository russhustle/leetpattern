from typing import List


def nextPermutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = n - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    if i != 0:
        j = n - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

    left, right = i, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # [1, 3, 2]
nums = [1, 2, 3, 4, 6, 5]
nextPermutation(nums)
print(nums)  # [1, 2, 3, 5, 4, 6]
