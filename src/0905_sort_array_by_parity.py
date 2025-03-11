from typing import List


# Left Right Pointers
def sortArrayByParityLR(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        if not nums[left] % 2:
            left += 1
        else:
            while left < right and nums[right] % 2:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]

    return nums


# Fast Slow Pointers
def sortArrayByParityFS(nums: List[int]) -> List[int]:
    n = len(nums)
    fast, slow = 0, 0

    while fast < n:
        if not nums[fast] % 2:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1

    return nums


nums = [3, 1, 2, 4]
print(sortArrayByParityLR(nums))  # [4, 2, 1, 3]
print(sortArrayByParityFS(nums))  # [4, 2, 1, 3]
