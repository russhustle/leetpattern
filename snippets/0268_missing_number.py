from typing import List


# Math
def missingNumberMath(nums: List[int]) -> int:
    n = len(nums)
    return (n * (n + 1)) // 2 - sum(nums)


# Bit Manipulation (XOR)
def missingNumberXOR(nums: List[int]) -> int:
    n = len(nums)

    for i, num in enumerate(nums):
        n ^= i ^ num

    return n


nums = [3, 0, 1]
print(missingNumberMath(nums))  # 2
print(missingNumberXOR(nums))  # 2
