from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    fast, slow = 2, 2

    while fast < len(nums):
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums))
