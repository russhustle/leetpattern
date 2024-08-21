from collections import defaultdict
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    hashmap = defaultdict(int)
    result = []

    for i in nums1:
        hashmap[i] += 1

    for i in nums2:
        if hashmap[i] > 0:
            result.append(i)
            hashmap[i] -= 1

    return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # [2, 2]
