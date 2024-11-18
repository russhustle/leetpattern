from typing import List


# Array
def validMountainArray(arr: List[int]) -> bool:
    n = len(arr)
    i = 0

    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1


# Left Right Pointers
def validMountainArrayLP(arr: List[int]) -> bool:
    n = len(arr)

    if n < 3:
        return False

    left, right = 0, n - 1

    while left < n - 1 and arr[left] < arr[left + 1]:
        left += 1

    while right > 0 and arr[right] < arr[right - 1]:
        right -= 1

    return 0 < left == right < n - 1


arr = [0, 3, 2, 1]
print(validMountainArray(arr))  # True
print(validMountainArrayLP(arr))  # True
