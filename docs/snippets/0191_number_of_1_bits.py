# Bit Manipulation
def hammingWeight1(n: int) -> int:
    res = 0

    while n != 0:
        n = n & (n - 1)  # Unset the rightmost 1-bit
        res += 1

    return res


def hammingWeight2(n: int) -> int:
    return bin(n).count("1")


def hammingWeight3(n: int) -> int:
    def decimalToBinary(n: int) -> str:
        if n == 0:
            return "0"

        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2

        return binary

    binary = decimalToBinary(n)

    return binary.count("1")


n = 11
print(hammingWeight1(n))  # 3
print(hammingWeight2(n))  # 3

n = 47
print(bin(n))
