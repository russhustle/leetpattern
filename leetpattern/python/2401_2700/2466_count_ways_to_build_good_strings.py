from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """Top-Down DP: O(high) time, O(high) space.
        Count strings by final length after appending zero-sized
        or one-sized blocks.
        """
        MOD = 1_000_000_007

        @cache
        def dfs(i):
            if i < 0:
                return 0
            if i == 0:
                return 1

            return (dfs(i - zero) + dfs(i - one)) % MOD

        return sum(dfs(i) for i in range(low, high + 1)) % MOD


def test_count_good_strings():
    s = Solution()
    assert s.countGoodStrings(3, 3, 1, 1) == 8
    assert s.countGoodStrings(2, 3, 1, 2) == 5
    assert s.countGoodStrings(1, 1, 1, 2) == 1
