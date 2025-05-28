"""
- [教你一步步思考 DP：从记忆化搜索到递推（Python/Java/C++/Go）](https://leetcode.cn/problems/palindrome-partitioning-ii/solutions/3588633/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-bnlb)
"""

from functools import cache


# Memoization
def minCutMemoization(s: str) -> int:
    @cache
    def is_palindrome(left, right):
        if left >= right:
            return True
        return s[left] == s[right] and is_palindrome(left + 1, right - 1)

    @cache
    def dfs(right):
        if is_palindrome(0, right):
            return 0
        res = float("inf")
        for left in range(1, right + 1):
            if is_palindrome(left, right):
                res = min(res, 1 + dfs(left - 1))
        return res

    return dfs(len(s) - 1)


# Tabulation
def minCutTabulation(s: str) -> int:
    n = len(s)
    is_palindrome = [[True] * n for _ in range(n)]

    for left in range(n - 2, -1, -1):
        for right in range(left + 1, n):
            is_palindrome[left][right] = (
                s[left] == s[right] and is_palindrome[left + 1][right - 1]
            )

    dp = [0 for _ in range(n)]

    for right, is_pal in enumerate(is_palindrome[0]):
        if is_pal:
            continue
        res = float("inf")
        for left in range(1, right + 1):
            if is_palindrome[left][right]:
                res = min(res, 1 + dp[left - 1])
        dp[right] = res

    return dp[-1]


s = "aab"
print(minCutMemoization(s))  # 1
print(minCutTabulation(s))  # 1
