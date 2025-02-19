from typing import List


# Array
def replaceElements(arr: List[int]) -> List[int]:
    n = len(arr)
    if n == 1:
        return [-1]

    rightMax = -1
    for i in range(n - 1, -1, -1):
        arr[i], rightMax = rightMax, max(rightMax, arr[i])

    return arr


arr = [17, 18, 5, 4, 6, 1]
print(replaceElements(arr))  # [18, 6, 6, 6, 1, -1]
