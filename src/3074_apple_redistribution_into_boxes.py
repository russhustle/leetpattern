from typing import List


# Greedy
def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
    target = sum(apple)
    capacity.sort(reverse=True)
    res = 0

    for box in capacity:
        res += 1
        target -= box
        if target <= 0:
            break

    return res


apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
assert minimumBoxes(apple, capacity) == 2
