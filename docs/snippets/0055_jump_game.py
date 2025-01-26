from typing import List


# Greedy - Interval
def canJump(nums: List[int]) -> bool:
    maxReach = 0
    i = 0
    n = len(nums)

    while i <= maxReach:
        maxReach = max(maxReach, i + nums[i])
        if maxReach >= n - 1:
            return True
        i += 1

    return False


print(canJump([2, 3, 1, 1, 4, 1, 2, 0, 0]))  # True
