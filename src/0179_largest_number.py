from functools import cmp_to_key
from typing import List


# Greedy
def largestNumber(nums: List[int]) -> str:
    strs = map(str, nums)

    def cmp(a, b):
        if a + b == b + a:
            return 0
        elif a + b > b + a:
            return 1
        else:
            return -1

    strs = sorted(strs, key=cmp_to_key(cmp), reverse=True)

    return "".join(strs) if strs[0] != "0" else "0"


nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))  # 9534330
