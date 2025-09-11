from collections import defaultdict
from typing import List


# Enumerate Right Maintain Left
def maxOperations(nums: List[int], k: int) -> int:
    counts = defaultdict(int)

    res = 0
    for num in nums:
        if num >= k:
            continue

        j = k - num
        if j in counts:
            res += 1
            counts[j] -= 1
            if counts[j] == 0:
                del counts[j]
        else:
            counts[num] += 1

    return res


if __name__ == "__main__":
    assert maxOperations([1, 2, 3, 4], 5) == 2
    assert maxOperations([3, 1, 3, 4, 3], 6) == 1
