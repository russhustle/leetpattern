# DP
def numDecodingsDP(s: str) -> int:
    if not s or s[0] == "0":
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        # Check single digit decode
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]

        # Check two digit decode
        if i > 1 and "10" <= s[i - 2 : i] <= "26":
            dp[i] += dp[i - 2]

    return dp[n]


# DFS
def numDecodingsDFS(s: str) -> int:
    memo = {}

    def dfs(i):
        if i == len(s):
            return 1

        if s[i] == "0":
            return 0

        if i in memo:
            return memo[i]

        # Single digit decode
        ways = dfs(i + 1)

        # Two digits decode
        if i + 1 < len(s) and "10" <= s[i : i + 2] <= "26":
            ways += dfs(i + 2)

        memo[i] = ways

        return ways

    return dfs(0)


s = "226"
print(numDecodingsDP(s))  # 3
print(numDecodingsDFS(s))  # 3
