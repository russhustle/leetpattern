from math import isqrt
from typing import List


# Prime
def diagonalPrime(nums: List[List[int]]) -> int:
    def is_prime(n):
        if n <= 1:
            return False

        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    res = 0
    for i, row in enumerate(nums):
        for x in row[i], row[-1 - i]:
            if x > res and is_prime(x):
                res = x

    return res


if __name__ == "__main__":
    nums = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
    print(diagonalPrime(nums))  # 11
