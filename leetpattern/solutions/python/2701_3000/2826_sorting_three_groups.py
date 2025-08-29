from functools import cache
from typing import List


# DP - LIS
def minimumOperationsMemo(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    @cache
    def dfs(i):
        res = 0
        for j in range(i):
            if nums[i] >= nums[j]:
                res = max(res, dfs(j))
        return res + 1

    LIS = max(dfs(i) for i in range(n))

    return n - LIS


# DP - LIS
def minimumOperationsTable(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)


# DP - LIS
def minimumOperationsTableOptimized(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    dp = [0 for _ in range(4)]

    for num in nums:
        dp[num] += 1
        dp[2] = max(dp[2], dp[1])
        dp[3] = max(dp[3], dp[2])

    return n - dp[3]


if __name__ == "__main__":
    assert minimumOperationsMemo([2, 1, 3, 2, 1]) == 3
    assert minimumOperationsTable([2, 1, 3, 2, 1]) == 3
    assert minimumOperationsTableOptimized([2, 1, 3, 2, 1]) == 3
