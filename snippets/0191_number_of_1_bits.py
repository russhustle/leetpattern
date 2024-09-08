# Bit Manipulation
def hammingWeight1(n: int) -> int:
    count = 0

    while n != 0:
        n = n & (n - 1)  # Unset the rightmost 1-bit
        count += 1

    return count


def hammingWeight2(n: int) -> int:
    return bin(n).count("1")


n = 11
print(hammingWeight1(n))  # 3
print(hammingWeight2(n))  # 3
