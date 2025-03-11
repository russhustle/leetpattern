from typing import List


# Math
def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    return [1] + digits


digits = [4, 3, 2, 1]
print(plusOne(digits))  # [4, 3, 2, 2]
