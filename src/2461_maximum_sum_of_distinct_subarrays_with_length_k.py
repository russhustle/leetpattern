from collections import defaultdict
from typing import List


# Sliding Window Fixed Size
def maximumSubarraySum(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    res = 0
    cur = 0

    for idx, num in enumerate(nums):
        counts[num] += 1
        cur += num

        if idx < k - 1:
            continue

        if len(counts) == k:
            res = max(res, cur)

        first = idx - k + 1
        cur -= nums[first]
        counts[nums[first]] -= 1
        if counts[nums[first]] == 0:
            del counts[nums[first]]

    return res


nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(maximumSubarraySum(nums, k))  # 15
