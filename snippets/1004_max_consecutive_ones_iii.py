from typing import List


# Sliding Window - Variable
def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    maxLen = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        maxLen = max(maxLen, right - left + 1)

    return maxLen


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longestOnes(nums, k))  # 6
