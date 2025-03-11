from typing import List


def removeDuplicates(nums: List[int]) -> int:
    fast, slow = 1, 1

    while fast < len(nums):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


nums = [1, 1, 2]
print(removeDuplicates(nums))  # 2
