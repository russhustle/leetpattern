from typing import List


# Greedy - Interval
def canJump(nums: List[int]) -> bool:
    reach = 0
    i = 0
    n = len(nums)

    while i <= reach:
        reach = max(reach, i + nums[i])
        if reach >= n - 1:
            return True
        i += 1

    return False


print(canJump([2, 3, 1, 1, 4]))  # True
