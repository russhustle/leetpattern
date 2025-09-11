from bisect import bisect_left
from typing import List


# Binary Search
def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    res = 0

    for x in arr1:
        i = bisect_left(arr2, x - d)
        if i == len(arr2) or arr2[i] > x + d:
            res += 1

    return res


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))  # 2
