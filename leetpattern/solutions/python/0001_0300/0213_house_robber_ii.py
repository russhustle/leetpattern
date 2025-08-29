"""
-   Return the maximum amount of money that can be robbed from the houses arranged in a circle.
-   Circular → Linear: `nums[0]` and `nums[-1]` cannot be robbed together.
-   Rob from `0` to `n - 2`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  0  |     2     |     -     |     2     |          -          |    2    |
|  1  |     7     |     -     |     7     |          -          |    7    |
|  2  |     9     |     2     |     7     |         11          |   11    |
|  3  |     3     |     7     |    11     |         10          |   11    |

-   Rob from `1` to `n - 1`

|  n  | `nums[n]` | `dp[n-2]` | `dp[n-1]` | `dp[n-2] + nums[n]` | `dp[n]` |
| :-: | :-------: | :-------: | :-------: | :-----------------: | :-----: |
|  1  |     7     |     -     |     -     |          -          |    7    |
|  2  |     9     |     -     |     7     |          -          |    9    |
|  3  |     3     |     7     |     9     |         10          |   10    |
|  4  |     1     |     9     |    10     |         10          |   10    |
"""

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
