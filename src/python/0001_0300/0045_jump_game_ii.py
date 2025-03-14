from typing import List


# Greedy (Interval)
def jump(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0

    maxReach = 0
    left, right = 0, 0
    res = 0

    while right < n - 1:
        for i in range(left, right + 1):
            maxReach = max(maxReach, i + nums[i])

        left = right + 1
        right = maxReach
        res += 1

    return res


print(jump([2, 3, 1, 1, 4, 2, 1]))  # 3
