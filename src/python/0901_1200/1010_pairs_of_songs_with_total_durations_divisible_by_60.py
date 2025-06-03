from collections import defaultdict
from typing import List


# Enumerate Right Maintain Left
def numPairsDivisibleBy60(time: List[int]) -> int:
    if not time or len(time) < 2:
        return 0

    count = defaultdict(int)
    res = 0
    time = [t % 60 for t in time]

    for t in time:
        if t == 0:
            res += count[0]
        else:
            res += count[60 - t]
        count[t] += 1

    return res


if __name__ == "__main__":
    assert numPairsDivisibleBy60([30, 20, 150, 100, 40]) == 3
    assert numPairsDivisibleBy60([60, 60, 60]) == 3
    assert numPairsDivisibleBy60([10, 50, 30, 20, 40]) == 2
