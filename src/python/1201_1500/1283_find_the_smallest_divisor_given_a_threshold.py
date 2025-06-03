"""
- 二分答案的关键是找到单调性，然后分析出判断条件
"""

from typing import List


# Binary Search Min Answer
def smallestDivisor(nums: List[int], threshold: int) -> int:
    left, right = 0, max(nums)

    while left + 1 < right:
        mid = left + (right - left) // 2
        if sum((x - 1) // mid for x in nums) <= threshold - len(nums):
            right = mid
        else:
            left = mid

    return right


if __name__ == "__main__":
    nums = [1, 2, 5, 9]
    threshold = 6
    assert smallestDivisor(nums, threshold) == 5
