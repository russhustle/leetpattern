from collections import defaultdict
from typing import List


# Hash
def maxSumHash(nums: List[int]) -> int:
    def find(num):
        res = 0
        while num != 0:
            num, carry = divmod(num, 10)
            res = max(res, carry)
        return res

    freqs = defaultdict(list)

    for num in nums:
        x = find(num)
        freqs[x].append(num)

    res = -1
    for vals in freqs.values():
        if len(vals) > 1:
            vals = sorted(vals, reverse=True)
            res = max(res, sum(vals[:2]))

    return res


# Array
def maxSumArray(nums: List[int]) -> int:
    res = -1
    max_val = [float("-inf") for _ in range(10)]

    for num in nums:
        maxDigit = max(map(int, str(num)))
        res = max(res, num + max_val[maxDigit])
        max_val[maxDigit] = max(max_val[maxDigit], num)

    return res


nums = [2536, 1613, 3366, 162]
print(maxSumHash(nums))  # 5902
print(maxSumArray(nums))  # 5902
