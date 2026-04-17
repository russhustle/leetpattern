class longestPalindrome:
    """Return the longest palindromic substring in s."""

    @staticmethod
    def dp(s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        start, maxLen = 0, 1

        # Init
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        # update
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                    if dp[i][j] and j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        start = i

        return s[start : start + maxLen]

    @staticmethod
    def expand_around_center(s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if len(s) <= 1:
            return s

        start, end = 0, 0
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            maxLen = max(odd, even)
            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2

        return s[start : end + 1]


if __name__ == "__main__":
    s = "babad"
    assert longestPalindrome.dp(s) in ["bab", "aba"]
    assert longestPalindrome.expand_around_center(s) in ["bab", "aba"]
