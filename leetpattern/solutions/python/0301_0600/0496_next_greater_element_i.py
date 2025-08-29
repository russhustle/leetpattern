from typing import List


# Monotonic Stack
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    next_greater = {}
    stack = []
    result = []

    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)

    for num in nums1:
        result.append(next_greater.get(num, -1))

    return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  # [3, -1, -1]
