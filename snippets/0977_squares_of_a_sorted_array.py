from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    result = [0 for _ in range(len(nums))]

    left, right, index = 0, len(nums) - 1, len(nums) - 1

    while left <= right:
        if abs(nums[left]) >= abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1
        index -= 1

    return result


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  # [0, 1, 9, 16, 100]
