from typing import List


# DP - LIS
def minDeletionSize(strs: List[str]) -> int:
    if not strs:
        return 0

    n = len(strs[0])
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if all(row[j] <= row[i] for row in strs):
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)
