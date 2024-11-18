from typing import List


# Left Right Pointers
def longestMountain(arr: List[int]) -> int:
    n = len(arr)
    res = 0
    left = 0

    while left < n:
        right = left

        if right < n - 1 and arr[right] < arr[right + 1]:
            while right < n - 1 and arr[right] < arr[right + 1]:
                right += 1

            if right < n - 1 and arr[right] > arr[right + 1]:
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                res = max(res, right - left + 1)

        left = max(right, left + 1)

    return res


arr = [2, 1, 4, 7, 3, 2, 5]
print(longestMountain(arr))  # 5
