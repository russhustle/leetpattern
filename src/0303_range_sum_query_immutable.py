from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0 for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
assert obj.sumRange(0, 2) == 1
assert obj.sumRange(2, 5) == -1
assert obj.sumRange(0, 5) == -3
print("PASSED")
