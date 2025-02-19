from typing import List


# Array
def maxDistance(arrays: List[List[int]]) -> int:
    mn, mx = float("inf"), float("-inf")
    res = 0

    for array in arrays:
        mn = min(mn, array[0])
        mx = max(mx, array[-1])
        res = max(res, abs(array[-1] - mn), abs(mx - array[0]))

    return res


arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
print(maxDistance(arrays))  # 4
