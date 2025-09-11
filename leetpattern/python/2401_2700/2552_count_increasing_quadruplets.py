from typing import List


# DP
def countQuadruplets(nums: List[int]) -> int:
    n = len(nums)
    great = [[0] * (n + 1) for _ in range(n)]
    less = [0 for _ in range(n + 1)]

    for k in range(n - 2, 1, -1):
        great[k] = great[k + 1].copy()
        for x in range(1, nums[k + 1]):
            great[k][x] += 1

    ans = 0

    for j in range(1, n - 1):
        for x in range(nums[j - 1] + 1, n + 1):
            less[x] += 1
        for k in range(j + 1, n - 1):
            if nums[j] > nums[k]:
                ans += less[nums[k]] * great[k][nums[j]]
    return ans


nums = [1, 3, 2, 4, 5]
print(countQuadruplets(nums))  # 2
