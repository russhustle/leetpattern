# Left Right Pointers
def mySqrt(x: int) -> int:
    """Returns the square root of a number."""
    if x < 2:
        return x

    left, right = 0, x // 2

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1


x = 8
print(mySqrt(x))  # 2
