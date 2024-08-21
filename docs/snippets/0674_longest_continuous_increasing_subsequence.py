from typing import List


def findLengthOfLCIS(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n

    dp = [1 for _ in range(n)]

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1

    return max(dp)


print(findLengthOfLCIS([1, 3, 5, 4, 7]))  # 3
