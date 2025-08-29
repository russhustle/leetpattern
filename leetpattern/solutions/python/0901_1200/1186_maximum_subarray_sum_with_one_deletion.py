"""
- [灵神：教你一步步思考动态规划 - 从记忆化搜索到递推](https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/solutions/2321829/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-hzz6))
"""

from functools import cache
from math import inf
from typing import List


# DP - Kadane
def maximumSum(arr: List[int]) -> int:
    dp0 = arr[0]
    dp1 = 0
    res = dp0

    for i in range(1, len(arr)):
        dp1 = max(dp1 + arr[i], dp0)  # delete previous element or not
        dp0 = max(dp0, 0) + arr[i]  # delete current element or not
        res = max(res, dp0, dp1)  # update result

    return res


# DP - Memoization
def maximumSumMemo(arr: List[int]) -> int:
    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0:
            return -inf
        if j == 0:
            return max(dfs(i - 1, 0), 0) + arr[i]
        return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))

    return max(max(dfs(i, 0), dfs(i, 1)) for i in range(len(arr)))


if __name__ == "__main__":
    arr = [1, -2, 0, 3]
    assert maximumSum(arr) == 4
    assert maximumSumMemo(arr) == 4
