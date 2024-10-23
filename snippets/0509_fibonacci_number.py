# DP
def fibDP(n: int) -> int:
    if n <= 1:
        return n

    dp = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Recursive
def fibRecursive(n: int) -> int:
    if n <= 1:
        return n

    return fibRecursive(n - 1) + fibRecursive(n - 2)


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |     DP      |      O(n)       |     O(n)     |
# |  Recursive  |     O(2^n)      |     O(n)     |
# |-------------|-----------------|--------------|


n = 10
print(fibDP(n))  # 55
print(fibRecursive(n))  # 55
