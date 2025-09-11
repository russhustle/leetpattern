from functools import reduce
from operator import or_
from typing import List


def subsetXORSum(nums: List[int]) -> int:
    return reduce(or_, nums) << (len(nums) - 1)


if __name__ == "__main__":
    nums = [5, 1, 6]
    print(subsetXORSum(nums))  # 28
