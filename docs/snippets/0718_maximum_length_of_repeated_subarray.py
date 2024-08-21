from typing import List


def findLength(nums1: List[int], nums2: List[int]) -> int:
    m = len(nums1)
    n = len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            if length < dp[i][j]:
                length = dp[i][j]

    return length


print(findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3
