# Bit Manipulation
def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0:
        temp = (a ^ b) & MASK
        b = ((a & b) << 1) & MASK
        a = temp

    return a if a <= MAX_INT else ~(a ^ MASK)


print(getSum(1, 2))  # 3
