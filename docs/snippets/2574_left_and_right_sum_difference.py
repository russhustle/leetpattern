from typing import List


# Prefix Sum
def leftRightDifferenceSum(nums: List[int]) -> List[int]:
    n = len(nums)
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]

    for i in range(1, n):
        left[i] = left[i - 1] + nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] + nums[i + 1]

    return [abs(left[i] - right[i]) for i in range(n)]


# Left Right Pointer
def leftRightDifferencePointer(nums: List[int]) -> List[int]:
    left, right = 0, sum(nums)
    result = []

    for num in nums:
        right -= num
        result.append(abs(left - right))
        left += num

    return result


nums = [10, 4, 8, 3]
print(leftRightDifferenceSum(nums))  # [15, 1, 11, 22]
print(leftRightDifferencePointer(nums))  # [15, 1, 11, 22]
