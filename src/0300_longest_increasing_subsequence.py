from typing import List


# DP - LIS
def lengthOfLIS(nums: List[int]) -> int:
    # TC: O(n^2)
    # SC: O(n)
    n = len(nums)
    if n <= 1:
        return n

    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # 4
