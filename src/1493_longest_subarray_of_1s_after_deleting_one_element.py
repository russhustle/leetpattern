from typing import List


# Sliding Window Variable Size
def longestSubarray(nums: List[int]) -> int:
    zeroCount = 0
    res = 0
    left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeroCount += 1

        while zeroCount > 1:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1

        res = max(res, right - left)

    return res


nums = [1, 1, 0, 1]
print(longestSubarray(nums))  # 3
