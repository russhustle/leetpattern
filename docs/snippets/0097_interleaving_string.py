# DP - 2D
def isInterleaveDP(s1: str, s2: str, s3: str) -> bool:
    m, n, k = len(s1), len(s2), len(s3)

    if m + n != k:
        return False

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            )

    return dp[m][n]


# DFS
def isInterleaveDFS(s1: str, s2: str, s3: str) -> bool:
    memo = {}

    def dfs(i, j, k):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True

        if (i, j) in memo:
            return memo[(i, j)]

        res = False

        if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
            res |= dfs(i + 1, j, k + 1)

        if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
            res |= dfs(i, j + 1, k + 1)

        memo[(i, j)] = res

        return res

    return dfs(0, 0, 0)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(isInterleaveDP(s1, s2, s3))  # False
print(isInterleaveDFS(s1, s2, s3))  # False
