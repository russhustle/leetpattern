from typing import List


# Sliding Window Fixed Size
def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    target = k * threshold
    res, cur = 0, 0

    for idx, num in enumerate(arr):
        cur += num

        if idx < k - 1:
            continue

        if cur >= target:
            res += 1

        cur -= arr[idx - k + 1]

    return res


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(numOfSubarrays(arr, k, threshold))  # 3
