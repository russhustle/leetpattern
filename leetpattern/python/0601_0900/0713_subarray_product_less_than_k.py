from typing import List


# Sliding Window Variable Subarrays Shorter
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    left = 0
    prod = 1
    res = 0

    for right in range(len(nums)):
        prod *= nums[right]

        while prod >= k:
            prod //= nums[left]
            left += 1

        res += right - left + 1

    return res


if __name__ == "__main__":
    assert numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert numSubarrayProductLessThanK([1, 2, 3], 0) == 0
    assert numSubarrayProductLessThanK([1, 2, 3], 1) == 0
    assert numSubarrayProductLessThanK([1, 2, 3], 2) == 1
    assert numSubarrayProductLessThanK([1, 2, 3], 3) == 3
