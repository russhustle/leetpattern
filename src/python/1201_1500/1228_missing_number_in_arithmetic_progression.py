from typing import List


def missingNumber(arr: List[int]) -> int:
    n = len(arr)
    s1 = (arr[0] + arr[-1]) * (n + 1) // 2
    s2 = sum(arr)
    return s1 - s2


# Binary Search
def missingNumberBS(arr: List[int]) -> int:
    n = len(arr)
    diff = (arr[-1] - arr[0]) // n

    left, right = 0, n - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == arr[0] + mid * diff:
            left = mid + 1
        else:
            right = mid

    return arr[0] + left * diff


if __name__ == "__main__":
    assert missingNumber([5, 7, 11, 13]) == 9
    assert missingNumber([15, 13, 12]) == 14
    assert missingNumber([1, 3]) == 2
    assert missingNumberBS([5, 7, 11, 13]) == 9
    assert missingNumberBS([15, 13, 12]) == 14
    assert missingNumberBS([1, 3]) == 2
