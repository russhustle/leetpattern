# Math
def reverse(x: int) -> int:
    INT_MAX = 2**31 - 1

    sign = -1 if x < 0 else 1
    x = abs(x)
    res = 0

    while x != 0:
        x, pop = divmod(x, 10)

        if res > (INT_MAX - pop) // 10:
            return 0

        res = res * 10 + pop

    return res * sign


print(reverse(123))  # 321
print(reverse(-123))  # -321
