"""
- Return the minimum number of jumps to reach the last index.
"""

from typing import List


# Greedy - Interval
def jump(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0

    reach = 0
    left, right = 0, 0
    res = 0

    while right < n - 1:
        for i in range(left, right + 1):
            reach = max(reach, i + nums[i])

        left = right + 1
        right = reach
        res += 1

    return res


if __name__ == "__main__":
    assert jump([2, 3, 1, 1, 4]) == 2
    assert jump([2, 3, 0, 1, 4]) == 2
