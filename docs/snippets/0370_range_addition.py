from typing import List


# Difference Array
def getModifiedArray(length: int, updates: List[List[int]]) -> List[int]:
    result = [0 for _ in range(length)]

    for start, end, inc in updates:
        result[start] += inc

        if end + 1 < length:
            result[end + 1] -= inc

    for i in range(1, length):
        result[i] += result[i - 1]

    return result


length = 5
updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
print(getModifiedArray(length, updates))  # [-2, 0, 3, 5, 3]
