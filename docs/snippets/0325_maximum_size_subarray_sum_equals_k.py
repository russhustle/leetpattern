from typing import List


# Prefix Sum
def maxSubArrayLen(nums: List[int], k: int) -> int:
    res = 0
    prefix = 0
    sumMap = {0: -1}  # sum -> index

    for i, num in enumerate(nums):
        prefix += num
        if prefix - k in sumMap:
            res = max(res, i - sumMap[prefix - k])
        if prefix not in sumMap:
            sumMap[prefix] = i

    return res


nums = [1, -1, 5, -2, 3]
k = 3
print(maxSubArrayLen(nums, k))  # 4
