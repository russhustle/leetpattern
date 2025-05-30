from collections import defaultdict
from typing import List


# Sliding Window Fixed Size
def distinctNumbers(nums: List[int], k: int) -> List[int]:
    res = []
    counts = defaultdict(int)

    for right in range(len(nums)):
        counts[nums[right]] += 1  # add

        if right < k - 1:  # form
            continue

        res.append(len(counts))  # update

        left = right - k + 1  # remove
        counts[nums[left]] -= 1
        if counts[nums[left]] == 0:
            del counts[nums[left]]

    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 2, 2, 1, 3]
    k = 3
    assert distinctNumbers(nums, k) == [3, 2, 2, 2, 3]
