def longestPalindromeSubseq(s: str) -> int:
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1

    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):

            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    return dp[0][-1]


print(longestPalindromeSubseq("bbbab"))  # 4
