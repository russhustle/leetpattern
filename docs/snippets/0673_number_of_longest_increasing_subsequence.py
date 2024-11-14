from typing import List


def findNumberOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    dp = [1 for _ in range(n)]
    counts = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    counts[i] = counts[j]
                elif dp[j] + 1 == dp[i]:
                    counts[i] += counts[j]

    longest = max(dp)
    return sum(c for i, c in enumerate(counts) if dp[i] == longest)


nums = [1, 3, 5, 4, 7]
print(findNumberOfLIS(nums))  # 2
