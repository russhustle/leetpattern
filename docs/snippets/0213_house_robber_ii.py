from typing import List


# DP
def rob(nums: List[int]) -> int:
    if len(nums) <= 3:
        return max(nums)

    def robLinear(nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    # circle -> linear
    a = robLinear(nums[1:])  # 2nd house to the last house
    b = robLinear(nums[:-1])  # 1st house to the 2nd last house

    return max(a, b)


nums = [2, 7, 9, 3, 1]
print(rob(nums))  # 11
