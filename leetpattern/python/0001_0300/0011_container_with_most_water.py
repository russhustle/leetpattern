from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Two Pointers: O(n) time, O(1) space.
        Move the shorter side inward to potentially find a taller line.
        """
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            res = max(res, w * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

    def maxAreaBF(self, height: List[int]) -> int:
        """Brute Force: O(n^2) time, O(1) space.
        Check every pair of lines.
        """
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res


def test_max_area():
    s = Solution()
    for fn in (s.maxArea, s.maxAreaBF):
        assert fn([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
        assert fn([1, 1]) == 1
        assert fn([4, 3, 2, 1, 4]) == 16
        assert fn([1, 2, 1]) == 2
