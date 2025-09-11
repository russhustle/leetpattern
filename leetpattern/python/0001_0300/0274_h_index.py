from typing import List


# Arrays
def hIndex(citations: List[int]) -> int:
    n = len(citations)
    cnt = [0 for _ in range(n + 1)]

    for c in citations:
        cnt[min(c, n)] += 1

    s = 0
    for i in range(n, -1, -1):
        s += cnt[i]
        if s >= i:
            return i


if __name__ == "__main__":
    assert hIndex([3, 0, 6, 1, 5]) == 3
    assert hIndex([1, 3, 1]) == 1
    assert hIndex([1, 2, 3, 4, 5]) == 3
    assert hIndex([0, 0, 0]) == 0
