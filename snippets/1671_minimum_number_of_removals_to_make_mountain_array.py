from typing import List


# DP - LIS
def minimumMountainRemovals(nums: List[int]) -> int:
    n = len(nums)
    lis = [1 for _ in range(n)]
    lds = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                lds[i] = max(lds[i], lds[j] + 1)

    maxLen = 0
    for i in range(1, n - 1):
        if lis[i] > 1 and lds[i] > 1:
            maxLen = max(maxLen, lis[i] + lds[i] - 1)

    return n - maxLen


nums = [2, 1, 1, 5, 6, 2, 3, 1]
print(minimumMountainRemovals(nums))  # 3
