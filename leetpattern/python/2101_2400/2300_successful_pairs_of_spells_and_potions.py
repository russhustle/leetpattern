import bisect
from typing import List


class successfulPairs:
    @staticmethod
    def binary_search(spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        res = []

        potions.sort()

        for spell in spells:
            target = (success + spell - 1) // spell
            index = bisect.bisect_left(potions, target)
            res.append(n - index)

        return res


if __name__ == "__main__":
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    assert successfulPairs.binary_search(spells, potions, success) == [4, 0, 3]
