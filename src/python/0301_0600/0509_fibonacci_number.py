from functools import cache


# DP
def fibDP(n: int) -> int:
    if n <= 1:
        return n

    dp = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# DP (Optimized)
def fibDPOptimized(n: int) -> int:
    if n <= 1:
        return n

    n1, n2 = 0, 1
    for _ in range(2, n + 1):
        n1, n2 = n2, n1 + n2

    return n2


# Recursive
@cache
def fibRecursive(n: int) -> int:
    if n <= 1:
        return n

    return fibRecursive(n - 1) + fibRecursive(n - 2)


n = 10
print(fibDP(n))  # 55
print(fibDPOptimized(n))  # 55
print(fibRecursive(n))  # 55
