from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    n = len(nums)
    prefix = [1 for _ in range(n)]
    suffix = [1 for _ in range(n)]

    for i in range(1, n):
        prefix[i] = nums[i - 1] * prefix[i - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = nums[i + 1] * suffix[i + 1]

    result = [i * j for i, j in zip(prefix, suffix)]

    return result


# Space optimized
def productExceptSelfOptimized(nums: List[int]) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(productExceptSelfOptimized([1, 2, 3, 4]))  # [24, 12, 8, 6]