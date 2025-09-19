from collections import defaultdict
from typing import List


# DP
def maximumLength(nums: List[int], k: int) -> int:
    count = [defaultdict(int) for _ in range(k + 1)]
    result = [0 for _ in range(k + 1)]

    for num in nums:
        for c in range(k, -1, -1):
            count[c][num] = max(count[c][num], result[c - 1] if c > 0 else 0) + 1
            result[c] = max(result[c], count[c][num])

    return max(result)


nums = [1, 2, 1, 1, 3]
k = 2
print(maximumLength(nums, k))  # 4
