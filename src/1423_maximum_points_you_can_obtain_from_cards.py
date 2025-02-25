from typing import List


# Sliding Window Fixed Size
def maxScore(cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    j = n - k
    total = sum(cardPoints)

    if j == 0:
        return total

    curSum, minSum = 0, float("inf")

    for idx, point in enumerate(cardPoints):
        curSum += point

        if idx < j - 1:
            continue

        minSum = min(minSum, curSum)
        curSum -= cardPoints[idx - j + 1]

    return total - minSum


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(maxScore(cardPoints, k))  # 12
