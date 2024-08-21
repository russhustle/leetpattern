# DP - LCS
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n <= 1:
        return s

    start, maxLen = 0, 1
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j]:
                if j - i <= 2:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start = i

    return s[start : start + maxLen]


s = "babad"
print(longestPalindrome(s))  # "bab" or "aba"
