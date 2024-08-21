# DP - LCS
def isSubsequenceLCS(s: str, t: str) -> bool:
    m = len(s)
    n = len(t)

    if m > n:
        return False

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1]  # only delete t string

            if length < dp[i][j]:
                length = dp[i][j]

    return length == m


# Two Pointers
def isSubsequenceTP(s: str, t: str) -> bool:
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


s = "abc"
t = "ahbgdc"
print(isSubsequenceLCS(s, t))  # True
print(isSubsequenceTP(s, t))  # True
