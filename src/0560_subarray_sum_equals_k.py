from collections import defaultdict
from typing import List


# Prefix Sum
def subarraySum(nums: List[int], k: int) -> int:
    preSums = defaultdict(int)
    preSums[0] = 1
    curSum = 0
    res = 0

    for num in nums:
        curSum += num
        res += preSums[curSum - k]
        preSums[curSum] += 1

    return res


nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # 2
