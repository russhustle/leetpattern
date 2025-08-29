from typing import List


# DP - LIS
def maxEnvelopes(envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []

    for w, h in envelopes:
        left, right = 0, len(dp)
        while left < right:
            mid = left + (right - left) // 2
            if dp[mid][1] < h:
                left = mid + 1
            else:
                right = mid
        if right == len(dp):
            dp.append((w, h))
        else:
            dp[right] = (w, h)

    return len(dp)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
print(maxEnvelopes(envelopes))  # 3
