from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Two Pointers: O(n) time, O(1) space.
        Swap non-zero elements to the front, zeroes drift to end.
        """
        slow = 0
        n = len(nums)

        for fast in range(n):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


def test_move_zeroes():
    s = Solution()
    for fn in (s.moveZeroes,):
        nums = [0, 1, 0, 3, 12]
        fn(nums)
        assert nums == [1, 3, 12, 0, 0]

        nums = [0]
        fn(nums)
        assert nums == [0]

        nums = [1, 2, 3]
        fn(nums)
        assert nums == [1, 2, 3]

        nums = [0, 0, 0, 0, 1]
        fn(nums)
        assert nums == [1, 0, 0, 0, 0]
