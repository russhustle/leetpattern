from typing import List


def removeElement(nums: List[int], val: int) -> int:
    fast, slow = 0, 0

    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))  # 2
