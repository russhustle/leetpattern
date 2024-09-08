from typing import List


# Left Right Pointers
def sortedSquares(nums: List[int]) -> List[int]:
    """Returns the squares of the sorted array."""
    n = len(nums)
    result = [0 for _ in range(n)]

    left, right, tail = 0, n - 1, n - 1

    while left <= right:
        if abs(nums[left]) >= abs(nums[right]):
            result[tail] = nums[left] ** 2
            left += 1
        else:
            result[tail] = nums[right] ** 2
            right -= 1
        tail -= 1

    return result


# |---------------------|------|-------|
# | Approach            | Time | Space |
# |---------------------|------|-------|
# | Left Right Pointers | O(n) | O(n)  |
# |---------------------|------|-------|


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  # [0, 1, 9, 16, 100]
