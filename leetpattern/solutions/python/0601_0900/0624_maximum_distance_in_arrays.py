from typing import List


# Array
def maxDistance(arrays: List[List[int]]) -> int:
    mn, mx = float("inf"), float("-inf")
    res = 0

    for arr in arrays:
        res = max(res, arr[-1] - mn, mx - arr[0])
        mn = min(mn, arr[0])
        mx = max(mx, arr[-1])

    return res


arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
print(maxDistance(arrays))  # 4
