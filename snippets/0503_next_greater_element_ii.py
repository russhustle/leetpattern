from typing import List


# Monotonic Stack
def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)

    return result


nums = [1, 2, 1]
print(nextGreaterElements(nums))  # [2, -1, 2]
