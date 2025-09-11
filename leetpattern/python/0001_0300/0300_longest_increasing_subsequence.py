from functools import cache
from typing import List


# DP - LIS
def lengthOfLISMemo(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n

    @cache
    def dfs(i: int) -> int:
        res = 0
        for j in range(i):
            if nums[j] < nums[i]:
                res = max(res, dfs(j))
        return res + 1

    return max(dfs(i) for i in range(n))


# DP - LIS
def lengthOfLISTable(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n

    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    assert lengthOfLISMemo([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lengthOfLISTable([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lengthOfLISMemo([0, 1, 0, 3, 2, 3]) == 4
    assert lengthOfLISTable([0, 1, 0, 3, 2, 3]) == 4
    assert lengthOfLISMemo([7, 7, 7, 7]) == 1
    assert lengthOfLISTable([7, 7, 7, 7]) == 1
