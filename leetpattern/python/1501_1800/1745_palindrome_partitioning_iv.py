# DP
def checkPartitioning(s: str) -> bool:
    def palidrome_partition(s, k):
        n = len(s)
        min_change = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                min_change[i][j] = min_change[i + 1][j - 1] + (1 if s[i] != s[j] else 0)

        dp = min_change[0]

        for i in range(1, k):
            for right in range(n - k + i, i - 1, -1):
                dp[right] = min(
                    dp[left - 1] + min_change[left][right] for left in range(i, right + 1)
                )

        return dp[-1]

    return palidrome_partition(s, 3) == 0


s = "abcbdd"
print(checkPartitioning(s))  # True
