from typing import List


# Right Left Pointers
def minimumRefill(plants: List[int], capacityA: int, capacityB: int) -> int:
    i, j = 0, len(plants) - 1
    a, b = capacityA, capacityB
    res = 0

    while i < j:
        if a < plants[i]:
            res += 1
            a = capacityA
        if b < plants[j]:
            res += 1
            b = capacityB

        a -= plants[i]
        b -= plants[j]
        i += 1
        j -= 1

    if i == j and max(a, b) < plants[i]:
        res += 1

    return res


if __name__ == "__main__":
    assert minimumRefill([2, 2, 3, 3], 5, 5) == 1
    assert minimumRefill([2, 2, 3, 3], 3, 4) == 2
    assert minimumRefill([5, 5], 10, 10) == 0
    assert minimumRefill([1, 2, 4, 4], 4, 4) == 1
    assert minimumRefill([1, 1, 1], 2, 2) == 0
