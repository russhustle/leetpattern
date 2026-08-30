from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Two Pointers: O(n) time, O(1) space.
        Keep `left` at the last unique value and overwrite the next position
        whenever `right` finds a different value.

        Example: nums = [0, 0, 1, 1, 2]
            start:   left = 0, unique prefix = [0]
            right 0: 0 == 0 -> unchanged
            right 1: 0 == 0 -> unchanged
            right 2: 1 != 0 -> left = 1, prefix = [0, 1]
            right 3: 1 == 1 -> unchanged
            right 4: 2 != 1 -> left = 2, prefix = [0, 1, 2]
        Return 3; the first three values are [0, 1, 2].
        """
        if not nums:
            return 0

        n = len(nums)
        left = 0

        for right in range(n):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left + 1


def test_remove_duplicates():
    s = Solution()
    for fn in (s.removeDuplicates,):
        cases = [
            ([], []),
            ([1], [1]),
            ([1, 1, 2], [1, 2]),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ]
        for nums, expected in cases:
            k = fn(nums)
            assert k == len(expected)
            assert nums[:k] == expected
