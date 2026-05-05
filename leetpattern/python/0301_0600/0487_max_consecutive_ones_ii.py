from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Sliding Window: O(n) time, O(1) space.
        Maintain a window with at most one 0; shrink from left when a second 0 enters.
        """
        left, zero, res = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1

            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


def test_find_max_consecutive_ones():
    s = Solution()
    for fn in (s.findMaxConsecutiveOnes,):
        assert fn([1, 0, 1, 1, 0]) == 4
        assert fn([1, 0, 1, 1, 0, 1]) == 4
        assert fn([1, 1, 1, 1]) == 4
        assert fn([0]) == 1
        assert fn([0, 0]) == 1
