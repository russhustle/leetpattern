# DP - LCS
def minDistance1(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no need to delete
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # delete word1[i]
                    dp[i][j - 1] + 1,  # delete word2[j]
                    dp[i - 1][j - 1] + 2,  # delete both
                )
    return dp[-1][-1]


# DP - LCS
def minDistance2(word1: str, word2: str) -> int:
    def LCS(word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        lcs = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                if lcs < dp[i][j]:
                    lcs = dp[i][j]
        return lcs

    lcs = LCS(word1, word2)
    return len(word1) + len(word2) - 2 * lcs


word1 = "sea"
word2 = "eat"
print(minDistance1(word1, word2))  # 2
print(minDistance2(word1, word2))  # 2
