from bisect import bisect_left
from typing import List


class searchRange:
    """
    找 lower bound 和 upper bound
    看灵神对这道题的题解，分类讨论区间的写法
    target 的 upper bound 是 target + 1 的 lower bound - 1
    这样就能统一用 lower bound 的写法
    """

    # [left, right]
    def bisect_left_closed(self, nums, target):
        """
        闭区间写法
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # [left, right)
    def bisect_left_right_open(self, nums, target):
        """
        左闭右开区间写法
        """
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    # (left, right)
    def bisect_left_open(self, nums, target):
        """
        推荐开区间写法
        """
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right

    def search_range(self, nums: List[int], target: int) -> List[int]:
        # edge case
        if not nums:
            return [-1, -1]

        lower = self.bisect_left_closed(nums, target)
        upper = self.bisect_left_closed(nums, target + 1) - 1

        return [lower, upper] if lower <= upper else [-1, -1]

    def search_range_bisect(self, nums: List[int], target: int) -> List[int]:
        """用 python bisect 库函数"""
        # edge case
        if not nums:
            return [-1, -1]

        lower = bisect_left(nums, target)
        upper = bisect_left(nums, target + 1) - 1

        return [lower, upper] if lower <= upper else [-1, -1]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    sol = searchRange()
    assert sol.search_range(nums, target) == [3, 4]
    assert sol.search_range_bisect(nums, target) == [3, 4]
