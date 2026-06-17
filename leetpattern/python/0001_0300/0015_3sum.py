from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Two Pointers: O(n^2) time, O(1) space.
        Sort, fix one element, then two-pointer scan for complement.
        """
        n = len(nums)
        if n <= 2:
            return []

        res = []
        nums.sort()

        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i, j = k + 1, n - 1

            while i < j:
                total = nums[k] + nums[i] + nums[j]

                if total > 0:
                    j -= 1
                elif total < 0:
                    i += 1
                else:
                    res.append([nums[k], nums[i], nums[j]])

                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1

                    i += 1
                    j -= 1

        return res


def test_three_sum():
    s = Solution()
    for fn in (s.threeSum,):
        assert fn([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
        assert fn([0, 1, 1]) == []
        assert fn([0, 0, 0]) == [[0, 0, 0]]
        assert fn([]) == []
