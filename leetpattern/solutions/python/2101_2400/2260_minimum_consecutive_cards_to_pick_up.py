from typing import List


# Enumerate Right Maintain Left
def minimumCardPickup(cards: List[int]) -> int:
    n = len(cards)
    res = n + 1
    last = {}

    for idx, card in enumerate(cards):
        if card in last:
            res = min(res, idx - last[card] + 1)
        last[card] = idx

    return res if res != n + 1 else -1


if __name__ == "__main__":
    assert minimumCardPickup([1, 2, 3, 4, 5]) == -1
    assert minimumCardPickup([1, 2, 3, 2, 3]) == 3
