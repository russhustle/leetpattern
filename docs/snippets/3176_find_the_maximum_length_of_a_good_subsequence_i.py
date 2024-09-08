from collections import defaultdict
from typing import List


# DP
def maximumLength(nums: List[int], k: int) -> int:
    frequency = defaultdict(lambda: [0 for _ in range(k + 1)])
    dp = [0 for _ in range(k + 1)]

    for num in nums:
        f = frequency[num]
        for j in range(k, -1, -1):
            f[j] += 1
            if j > 0:
                f[j] = max(f[j], dp[j - 1] + 1)
            dp[j] = max(f[j], dp[j])

    return dp[-1]


nums = [1, 2, 1, 1, 3]
k = 2
print(maximumLength(nums, k))  # 4
