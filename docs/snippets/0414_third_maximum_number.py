from typing import List


# 1. Sorting
def thirdMaxSort(nums: List[int]) -> int:
    nums = list(set(nums))
    nums.sort(reverse=True)

    return nums[2] if len(nums) >= 3 else nums[0]


# 2. Compare
def thirdMaxCompare(nums: List[int]) -> int:
    first, second, third = float("-inf"), float("-inf"), float("-inf")

    for num in nums:
        if num > first:
            first, second, third = num, first, second
        elif first > num > second:
            second, third = num, second
        elif second > num > third:
            third = num

    return third if third != float("-inf") else first


print(thirdMaxSort([3, 2, 1]))  # 1
print(thirdMaxCompare([3, 2, 1]))  # 1
