from functools import cache


class LongestCommonSubsequence:
    def memoization(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(m - 1, n - 1)

    def iterative(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i, x in enumerate(text1):
            for j, y in enumerate(text2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[-1][-1]


if __name__ == "__main__":
    lcs = LongestCommonSubsequence()
    assert lcs.memoization("abcde", "ace") == 3
    assert lcs.iterative("abcde", "ace") == 3
    assert lcs.memoization("abc", "abc") == 3
    assert lcs.iterative("abc", "abc") == 3
