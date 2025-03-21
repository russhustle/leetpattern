from functools import cache


# Recursive
def minDistanceDFS(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)

    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if word1[i] == word2[j]:
            return dfs(i - 1, j - 1)

        return 1 + min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1))

    return dfs(n - 1, m - 1)


# Iterative
def minDistanceDP(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no operation
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # delete
                    dp[i][j - 1],  # insert
                    dp[i - 1][j - 1],  # replace
                )
    return dp[-1][-1]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(minDistanceDFS(word1, word2))  # 3
    print(minDistanceDP(word1, word2))  # 3
