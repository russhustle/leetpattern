"""
-   Return the maximum product of the integer after breaking it into at least two positive integers.
-   `dp[i]` stores the maximum product of the integer `i`.
-   Formula: `dp[i] = max(dp[i - j] * j, (i - j) * j)`
-   Time Complexity: O(n^2)
-   Space Complexity: O(n)

| dp        | 3       | 4       | 5       | 6       | 7        | 8        |
|:---------:|:-------:|:-------:|:-------:|:-------:|:--------:|:--------:|
| 2         | 2*1=2   | 2*2=4   | 2*3=6   | 2*4=8   | 2*5=10   | 2*6=12   |
| dp[2]=1   | 1*1=1   | 1*2=2   | 1*3=3   | 1*4=4   | 1*5=5    | 1*6=6    |
| 3         |         | 3*1=3   | 3*2=6   | 3*3=9   | 3*4=12   | 3*5=15   |
| dp[3]=2   |         | 2*1=2   | 2*2=4   | 2*3=6   | 2*4=8    | 2*5=10   |
| 4         |         |         | 4*1=4   | 4*2=8   | 4*3=12   | 4*4=16   |
| dp[4]=4   |         |         | 4*1=4   | 4*2=8   | 4*3=12   | 4*4=16   |
| 5         |         |         |         | 5*1=5   | 5*2=10   | 5*3=15   |
| dp[5]=6   |         |         |         | 6*1=6   | 6*2=12   | 6*3=18   |
| 6         |         |         |         |         | 6*1=6    | 6*2=12   |
| dp[6]=9   |         |         |         |         | 9*1=9    | 9*2=18   |
| 7         |         |         |         |         |          | 7*1=7    |
| dp[7]=12  |         |         |         |         |          | 12*1=12  |
| `dp[n]`   | 2       | 4       | 6       | 9       | 12       | 18       |
"""


def integerBreak(n: int) -> int:
    dp = [0 for _ in range(n + 1)]
    dp[2] = 1

    for i in range(3, n + 1):
        for j in range(2, i):
            dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)

    return dp[n]


if __name__ == "__main__":
    print(integerBreak(8))  # 18
