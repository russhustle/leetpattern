# DP - LCS
def longestCommonSubsequence(text1: str, text2: str) -> int:
    # TC: O(m * n)
    # SC: O(m * n)
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            if length < dp[i][j]:
                length = dp[i][j]

    return length


text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))  # 3
