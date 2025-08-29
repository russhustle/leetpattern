from typing import List


# DP (House Robber)
def deleteAndEarn(nums: List[int]) -> int:
    def rob(nums):
        f0, f1 = 0, 0
        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)
        return f1

    res = [0 for _ in range(max(nums) + 1)]

    for x in nums:
        res[x] += x

    return rob(res)


nums = [2, 2, 3, 3, 3, 4]
print(deleteAndEarn(nums))  # 9
