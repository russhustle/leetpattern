from typing import List


# DP - Kadane
def maxTurbulenceSize(arr: List[int]) -> int:
    n = len(arr)
    up = [1 for _ in range(n)]
    down = [1 for _ in range(n)]
    maxLen = 1

    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            up[i] = down[i - 1] + 1
            down[i] = 1
        elif arr[i - 1] > arr[i]:
            down[i] = up[i - 1] + 1
            up[i] = 1
        else:
            up[i] = 1
            down[i] = 1

        maxLen = max(maxLen, up[i], down[i])

    return maxLen


arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
print(maxTurbulenceSize(arr))  # 5
