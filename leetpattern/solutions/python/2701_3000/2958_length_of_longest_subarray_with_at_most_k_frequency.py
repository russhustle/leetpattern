from collections import defaultdict
from typing import List


# Sliding Window Variable Size
def maxSubarrayLength(nums: List[int], k: int) -> int:
    n = len(nums)
    freqs = defaultdict(int)  # num -> freq
    left = 0
    res = 0

    for right in range(n):
        freqs[nums[right]] += 1

        while freqs[nums[right]] > k:
            freqs[nums[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


nums = [1, 2, 1, 2, 1, 2, 1, 2]
k = 2
print(maxSubarrayLength(nums, k))  # 4
