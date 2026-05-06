from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Set: O(n) time, O(n) space.
        Track seen elements; return True on first repeat.
        """
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

    def containsDuplicateSort(self, nums: List[int]) -> bool:
        """Sort: O(n log n) time, O(1) space.
        Duplicates become adjacent after sorting.
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def containsDuplicateBF(self, nums: List[int]) -> bool:
        """Brute Force: O(n^2) time, O(1) space.
        Compare every pair.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


def test_contains_duplicate():
    s = Solution()
    for fn in (s.containsDuplicate, s.containsDuplicateSort, s.containsDuplicateBF):
        assert fn([1, 2, 3, 1]) is True
        assert fn([1, 2, 3, 4]) is False
        assert fn([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
        assert fn([]) is False
