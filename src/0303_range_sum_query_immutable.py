from typing import List


# Prefix Sum
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.ps = [0 for _ in range(n + 1)]  # prefix sum
        for i in range(1, n + 1):
            self.ps[i] = self.ps[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right + 1] - self.ps[left]


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
assert obj.sumRange(0, 2) == 1
assert obj.sumRange(2, 5) == -1
assert obj.sumRange(0, 5) == -3
print("PASSED")
