from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Two Pointers: O(n) time, O(1) space.
        Track max from each side; shorter side determines water level.
        """
        left, right = 0, len(height) - 1
        max_l = max_r = res = 0
        while left < right:
            if height[left] < height[right]:
                max_l = max(max_l, height[left])
                res += max_l - height[left]
                left += 1
            else:
                max_r = max(max_r, height[right])
                res += max_r - height[right]
                right -= 1
        return res

    def trapDP(self, height: List[int]) -> int:
        """DP Prefix Max: O(n) time, O(n) space.
        Precompute max heights from left and right.
        """
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        return sum(max(0, min(max_left[i], max_right[i]) - height[i]) for i in range(n))

    def trapStack(self, height: List[int]) -> int:
        """Monotonic Stack: O(n) time, O(n) space.
        Pop shorter bars and accumulate trapped water by layer.
        """
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                w = i - stack[-1] - 1
                h = min(height[i], height[stack[-1]]) - height[top]
                res += w * h
            stack.append(i)
        return res


def test_trap():
    s = Solution()
    for fn in (s.trap, s.trapDP, s.trapStack):
        assert fn([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
        assert fn([4, 2, 0, 3, 2, 5]) == 9
        assert fn([1, 0, 1]) == 1
        assert fn([]) == 0
