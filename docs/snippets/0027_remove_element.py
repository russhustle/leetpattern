from typing import List


# Fast Slow Pointers
def removeElement(nums: List[int], val: int) -> int:
    fast, slow = 0, 0

    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))  # 5
