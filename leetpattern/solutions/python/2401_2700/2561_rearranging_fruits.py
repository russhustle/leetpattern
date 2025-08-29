from collections import defaultdict
from typing import List


def minCost(basket1: List[int], basket2: List[int]) -> int:
    cnt = defaultdict(int)
    for x, y in zip(basket1, basket2):
        cnt[x] += 1
        cnt[y] -= 1

    a, b = [], []
    for x, c in cnt.items():
        if c % 2:
            return -1

        if c > 0:
            a.extend([x] * (c // 2))
        else:
            b.extend([x] * (-c // 2))

    a.sort()
    b.sort(reverse=True)
    mn = min(cnt)

    return sum(min(x, y, mn * 2) for x, y in zip(a, b))


if __name__ == "__main__":
    basket1 = [4, 2, 2, 2]
    basket2 = [1, 4, 1, 2]
    assert minCost(basket1, basket2) == 1
