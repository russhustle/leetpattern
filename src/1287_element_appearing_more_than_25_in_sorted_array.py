from bisect import bisect_left, bisect_right
from typing import List


# Binary Search
def findSpecialInteger(arr: List[int]) -> int:
    n = len(arr)
    span = n // 4 + 1

    for i in range(0, n, span):
        left = bisect_left(arr, arr[i])
        right = bisect_right(arr, arr[i])
        if right - left >= span:
            return arr[i]

    return -1
