from functools import cache


# DP - LCS
def longestCommonSubsequenceMemo(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0
        if text1[i] == text2[j]:
            return dfs(i - 1, j - 1) + 1
        return max(dfs(i - 1, j), dfs(i, j - 1))

    return dfs(m - 1, n - 1)


# DP - LCS
def longestCommonSubsequenceTable(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


if __name__ == "__main__":
    assert longestCommonSubsequenceMemo("abcde", "ace") == 3
    assert longestCommonSubsequenceTable("abcde", "ace") == 3
    assert longestCommonSubsequenceMemo("abc", "abc") == 3
    assert longestCommonSubsequenceTable("abc", "abc") == 3
