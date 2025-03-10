from functools import reduce
from operator import xor
from typing import List


# XOR
def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res


# XOR
def singleNumberXOR(nums: List[int]) -> int:
    return reduce(xor, nums)


# XOR
def singleNumberXORLambda(nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # 4
print(singleNumberXOR(nums))  # 4
print(singleNumberXORLambda(nums))  # 4
