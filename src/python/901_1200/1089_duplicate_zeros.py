from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    fast, slow = 0, 0

    # First pass: find the position
    # where the last element would be in the expanded array
    while fast < n:
        if arr[slow] == 0:
            fast += 1
        slow += 1
        fast += 1

    slow -= 1
    fast -= 1

    # Second pass: move elements backwards
    while slow >= 0:
        if fast < n:
            arr[fast] = arr[slow]

        if arr[slow] == 0:
            fast -= 1
            if fast < n:
                arr[fast] = 0

        slow -= 1
        fast -= 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr)
print(arr)  # [1, 0, 0, 2, 3, 0, 0, 4]
