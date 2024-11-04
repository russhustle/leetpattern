def countSubstrings(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    res = 0

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = 1
                    res += 1
                elif dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    res += 1

    return res


print(countSubstrings("abbae"))  # 7
