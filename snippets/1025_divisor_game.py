# DP
def divisorGameDP(n: int) -> bool:
    if n <= 1:
        return False

    dp = [False for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0 and not dp[i - j]:
                dp[i] = True
                break

    return dp[n]


# Math
def divisorGameDPMath(n: int) -> bool:
    return n % 2 == 0


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |  DP         |      O(n^2)     |    O(n)      |
# |  Math       |      O(1)       |    O(1)      |
# |-------------|-----------------|--------------|

n = 2
print(divisorGameDP(n))  # True
print(divisorGameDPMath(n))  # True
