"""
-   Return the minimum number of jumps to reach the last index.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dJ7sWiOoK7g?si=3kc-pp4rs3Dk7Jqk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
"""

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
