"""
- Return `True` if you can reach the last index, otherwise `False`.
"""

from typing import List


# Greedy - Interval
def canJump(nums: List[int]) -> bool:
    n = len(nums)
    reach = 0
    i = 0

    while reach >= i:
        if reach >= n - 1:
            return True
        reach = max(reach, i + nums[i])
        i += 1

    return False


if __name__ == "__main__":
    assert canJump([2, 3, 1, 1, 4]) is True
    assert canJump([3, 2, 1, 0, 4]) is False
