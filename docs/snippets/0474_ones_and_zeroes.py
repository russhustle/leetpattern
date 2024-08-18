from typing import List


def findMaxForm(strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
        zerosNum = s.count("0")
        onesNum = len(s) - zerosNum

        for i in range(m, zerosNum - 1, -1):
            for j in range(n, onesNum - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zerosNum][j - onesNum] + 1)

    return dp[m][n]


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(findMaxForm(strs, m, n))  # 4
