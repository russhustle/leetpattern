from typing import List


# Bit Manipulation
def countBits(n: int) -> List[int]:
    bits = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)

    return bits


n = 5
print(countBits(n))  # [0, 1, 1, 2, 1, 2]
