from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        return gcd(max(nums), min(nums))
