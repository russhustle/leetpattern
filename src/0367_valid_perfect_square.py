# Binary Search
def isPerfectSquare(num: int) -> bool:
    if num < 2:
        return True

    left, right = 0, num // 2

    while left <= right:
        mid = left + (right - left) // 2

        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


num = 16
print(isPerfectSquare(num))  # True
