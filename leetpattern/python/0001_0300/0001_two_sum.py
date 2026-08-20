from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Hash Map: O(n) time, O(n) space.
        Store seen values so each number can find its complement in one pass.
        """
        hashmap = {}  # val: idx

        for idx, val in enumerate(nums):
            comp = target - val
            if comp in hashmap:
                return [hashmap[comp], idx]

            hashmap[val] = idx

        return []


def test_two_sum():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([1, 2, 3, 4, 5], 10) == []
    assert s.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
