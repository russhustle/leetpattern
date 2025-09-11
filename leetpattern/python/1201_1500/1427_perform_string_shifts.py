"""
-   Calculate the net shift direction and amount by combining all operations, then apply a single rotation to the string using slicing.
"""

from typing import List


def stringShift(s: str, shift: List[List[int]]) -> str:
    total_shift = 0
    for direction, amount in shift:
        if direction == 0:
            total_shift -= amount
        else:
            total_shift += amount

    total_shift %= len(s)

    if total_shift == 0:
        return s

    if total_shift > 0:
        return s[-total_shift:] + s[:-total_shift]
    else:
        total_shift = abs(total_shift)
        return s[total_shift:] + s[:total_shift]
