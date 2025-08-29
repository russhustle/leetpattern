from typing import List


# DP - LIS
def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    n = len(scores)
    pairs = sorted(zip(scores, ages))  # sort
    dp = [0 for _ in range(n)]

    # LIS
    for i in range(n):
        for j in range(i):
            if pairs[i][1] >= pairs[j][1]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += pairs[i][0]

    return max(dp)


if __name__ == "__main__":
    assert bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]) == 34
    assert bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]) == 16
