from typing import List


# Monotonic Stack
def find132pattern(nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False

    stack = []
    second_max = float("-inf")

    for i in range(n - 1, -1, -1):
        if nums[i] < second_max:
            return True

        while stack and stack[-1] < nums[i]:
            second_max = stack.pop()

        stack.append(nums[i])

    return False


nums = [-1, 3, 2, 0]
print(find132pattern(nums))  # True
