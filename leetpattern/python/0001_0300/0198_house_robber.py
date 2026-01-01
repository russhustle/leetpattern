from functools import cache
from typing import List


class Rob:
    """
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    """

    def incursive(self, nums: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        n = len(nums)
        if n <= 2:
            return max(nums)

        # init
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        # update
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    def incursive_optimized(self, nums: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        f0, f1 = 0, 0

        for num in nums:
            f0, f1 = f1, max(f1, f0 + num)

        return f1

    def memoization(self, nums: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        n = len(nums)

        @cache
        def dp(i: int) -> int:
            if i < 0:
                return 0
            return max(dp(i - 1), dp(i - 2) + nums[i])

        return dp(n - 1)


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    rob = Rob()
    assert rob.incursive(nums) == 12
    assert rob.incursive_optimized(nums) == 12
    assert rob.memoization(nums) == 12
