# DP (LCS)
def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Computes the length of the longest common subsequence between two strings.

    dp[i][j]: the length of the LCS between text1[:i] and text2[:j].

    Args:
        text1 (str): The first string.
        text2 (str): The second string.

    Returns:
        int: The length of the longest common subsequence.

    Example:
        >>> longestCommonSubsequence("abcde", "ace")
        3
        >>> longestCommonSubsequence("abc", "abc")
        3
        >>> longestCommonSubsequence("abc", "def")
        0
    """

    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
