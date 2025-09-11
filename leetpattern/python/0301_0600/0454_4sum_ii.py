"""
-   Return the number of tuples `(i, j, k, l)` such that `A[i] + B[j] + C[k] + D[l] == 0`.
"""

from collections import defaultdict
from typing import List


def fourSumCount(
    nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
) -> int:

    sumAB = defaultdict(int)
    result = 0

    for i in nums1:
        for j in nums2:
            sumAB[i + j] += 1

    for i in nums3:
        for j in nums4:
            if -(i + j) in sumAB:
                result += sumAB[-(i + j)]

    return result


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
print(fourSumCount(nums1, nums2, nums3, nums4))  # 2
