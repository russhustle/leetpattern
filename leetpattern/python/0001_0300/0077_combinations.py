from itertools import combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """Backtracking: O(k * C(n,k)) time, O(k) space.
        Prune by ensuring remaining elements suffice for k.
        """
        res = []

        def bt(start: int, path: List[int]) -> None:
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                bt(i + 1, path)
                path.pop()

        bt(1, [])
        return res

    def combineItertools(self, n: int, k: int) -> List[List[int]]:
        """Itertools: O(k * C(n,k)) time, O(k) space.
        Leverage stdlib combinations generator.
        """
        return [list(c) for c in combinations(range(1, n + 1), k)]


def test_combine():
    s = Solution()
    for fn in (s.combine, s.combineItertools):
        assert sorted(fn(4, 2)) == sorted(
            [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        )
        assert sorted(fn(4, 3)) == sorted([[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]])
        assert fn(1, 1) == [[1]]
