def countSubstrings(s: str) -> int:
    dp = [[False] * len(s) for _ in range(len(s))]
    result = 0

    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                if j - i <= 1:
                    dp[i][j] = True
                    result += 1
                elif dp[i + 1][j - 1]:
                    dp[i][j] = True
                    result += 1
    return result


print(countSubstrings("abc"))  # 3
