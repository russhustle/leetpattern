def divisorGame(n: int) -> bool:
    # Time complexity: O(n^2)
    # Space complexity: O(n)

    if n <= 1:
        return False

    dp = [False for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0 and not dp[i - j]:
                dp[i] = True
                break
    return dp[n]


n = 2
print(divisorGame(n))  # True
