# Binary Search
def firstBadVersion(n: int) -> int:
    left, right = 1, n

    while left <= right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


def isBadVersion(version: int) -> bool:
    pass
