from typing import List


# Sliding Window Variable Max
def minOperations(nums: List[int], x: int) -> int:
    window = 0
    total = sum(nums)
    target = total - x
    n = len(nums)
    left = 0
    maxLen = 0

    if target < 0:
        return -1
    if target == 0:
        return n

    for right in range(n):
        window += nums[right]

        while left <= right and window > target:
            window -= nums[left]
            left += 1

        if window == target:
            maxLen = max(maxLen, right - left + 1)

    return -1 if not maxLen else n - maxLen


if __name__ == "__main__":
    nums = [1, 1, 4, 2, 3]
    x = 5
    assert minOperations(nums, x) == 2
