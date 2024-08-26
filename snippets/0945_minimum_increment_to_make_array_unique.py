from typing import List


# Greedy
def minIncrementForUnique(nums: List[int]) -> int:
    nums.sort()
    moves = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            moves += nums[i - 1] + 1 - nums[i]
            nums[i] = nums[i - 1] + 1

    return moves


nums = [1, 2, 2]
print(minIncrementForUnique(nums))  # 1
