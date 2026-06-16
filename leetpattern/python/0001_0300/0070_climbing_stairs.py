from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        """Optimized DP: O(n) time, O(1) space.
        Only the previous two counts are needed to compute the next stair.
        """
        if n <= 2:
            return n

        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second
        return second

    def climbStairsDP(self, n: int) -> int:
        """Tabulation DP: O(n) time, O(n) space.
        Each stair count is the sum of the ways to reach the previous two stairs.
        """
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairsGreedy(self, n: int) -> int:
        """Greedy Rolling Counts: O(n) time, O(1) space.
        The next answer is always determined by the two latest reachable counts.
        """
        if n <= 2:
            return n

        prev, cur = 1, 2
        for _ in range(3, n + 1):
            prev, cur = cur, prev + cur
        return cur

    def climbStairsDFS(self, n: int) -> int:
        """Memoized DFS: O(n) time, O(n) space.
        Caching prevents recomputing the same remaining-stair subproblems.
        """

        @cache
        def dfs(i: int) -> int:
            if i <= 2:
                return i
            return dfs(i - 1) + dfs(i - 2)

        return dfs(n)


def test_climb_stairs():
    s = Solution()
    for fn in (
        s.climbStairs,
        s.climbStairsDP,
        s.climbStairsGreedy,
        s.climbStairsDFS,
    ):
        assert fn(1) == 1
        assert fn(2) == 2
        assert fn(3) == 3
        assert fn(10) == 89
