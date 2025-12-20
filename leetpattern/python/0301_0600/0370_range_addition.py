from typing import List


def getModifiedArray(length: int, updates: List[List[int]]) -> List[int]:
    """
    Return the final array after applying all the Adition operations.
    method: difference array
    """

    res = [0 for _ in range(length)]

    for start, end, inc in updates:
        res[start] += inc

        if end + 1 < length:
            res[end + 1] -= inc

    for i in range(1, length):
        res[i] += res[i - 1]

    return res


if __name__ == "__main__":
    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    assert getModifiedArray(length, updates) == [-2, 0, 3, 5, 3]
