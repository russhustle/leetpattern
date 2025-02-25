from collections import defaultdict
from typing import List


# Sliding Window Fixed Size
def maxSum(nums: List[int], m: int, k: int) -> int:
    counts = defaultdict(int)
    cur, res = 0, 0

    for idx, num in enumerate(nums):
        counts[num] += 1
        cur += num

        if idx < k - 1:
            continue

        if len(counts) >= m:
            res = max(res, cur)

        first = idx - k + 1
        cur -= nums[first]
        counts[nums[first]] -= 1
        if counts[nums[first]] == 0:
            del counts[nums[first]]

    return res


nums = [2, 6, 7, 3, 1, 7]
m = 3
k = 4
print(maxSum(nums, m, k))  # 18
