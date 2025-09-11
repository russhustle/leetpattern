from collections import Counter
from typing import List


# Sliding Window Fixed Size
def shareCandies(candies: List[int], k: int) -> int:
    res = 0
    n = len(candies)
    counts = Counter(candies)

    if k >= n:
        return 0
    if k == 0:
        return len(counts)

    for right in range(n):
        counts[candies[right]] -= 1  # remove
        if counts[candies[right]] == 0:
            del counts[candies[right]]

        if right < k - 1:  # form the window
            continue

        res = max(res, len(counts))  # update

        left = right - k + 1  # add
        counts[candies[left]] += 1

    return res


if __name__ == "__main__":
    candies = [1, 2, 2, 3, 4, 3]
    k = 3
    assert shareCandies(candies, k) == 3
