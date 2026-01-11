from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # edge case
        n = len(points)
        if n <= 2:
            return n

        res = 0

        for i in range(n - 1):
            x1, y1 = points[i]
            cnt = defaultdict(int)

            for j in range(i + 1, n):
                x2, y2 = points[j]
                g = "inf" if x1 == x2 else (y2 - y1) / (x2 - x1)
                cnt[g] += 1

            res = max(res, 1 + max(cnt.values()))

        return res


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    assert sol.maxPoints(points) == 4
