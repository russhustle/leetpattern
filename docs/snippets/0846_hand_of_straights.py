from collections import Counter
from typing import List


# Greedy
def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    count = Counter(hand)

    while count:
        minVal = min(count)
        for i in range(minVal, minVal + groupSize):
            if count[i] == 0:
                return False
            count[i] -= 1
            if count[i] == 0:
                del count[i]
    return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
print(isNStraightHand(hand, groupSize))  # True
