import bisect
from typing import List


# Binary Search
def successfulPairs(
    spells: List[int], potions: List[int], success: int
) -> List[int]:
    potions.sort()
    res = []
    n = len(potions)

    for spell in spells:
        target = (success + spell - 1) // spell
        index = bisect.bisect_left(potions, target)
        res.append(n - index)

    return res


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(successfulPairs(spells, potions, success))  # [4, 0, 3]
