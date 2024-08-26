from typing import List


# Greedy
def canJump(nums: List[int]) -> bool:
    n = len(nums)
    if n <= 1:
        return True

    maxReachable = 0
    i = 0

    while i <= maxReachable:
        maxReachable = max(maxReachable, i + nums[i])
        if maxReachable >= n - 1:
            return True
        i += 1

    return False


print(canJump([2, 3, 1, 1, 4]))  # True
