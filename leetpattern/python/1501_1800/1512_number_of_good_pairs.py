from collections import defaultdict
from typing import List


# Hash
def numIdenticalPairs(nums: List[int]) -> int:
    res = 0
    counts = defaultdict(int)  # num: count

    for num in nums:
        res += counts[num]
        counts[num] += 1

    return res


nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))  # 4
