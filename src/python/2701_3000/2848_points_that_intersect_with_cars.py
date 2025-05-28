"""
-   Return the number of points that intersect with cars.
"""

from itertools import accumulate
from typing import List


# Differnce Array
def numberOfPoints(nums: List[List[int]]) -> int:
    max_end = max(end for _, end in nums)

    diff = [0] * (max_end + 2)

    for start, end in nums:
        diff[start] += 1
        diff[end + 1] -= 1

    return sum(s > 0 for s in accumulate(diff))


nums = [[3, 6], [1, 5], [4, 7]]
print(numberOfPoints(nums))  # 7
