from typing import List


# Sliding Window - Variable
def maximizeWin(prizePositions: List[int], k: int) -> int:
    n = len(prizePositions)

    if 2 * k >= prizePositions[-1] - prizePositions[0]:
        return n

    ans = left = 0
    mx = [0] * (n + 1)

    for right, p in enumerate(prizePositions):
        while p - prizePositions[left] > k:
            left += 1
        ans = max(ans, mx[left] + right - left + 1)
        mx[right + 1] = max(mx[right], right - left + 1)

    return ans


prizePositions = [1, 1, 2, 2, 3, 3, 5]
k = 2
print(maximizeWin(prizePositions, k))  # 7
