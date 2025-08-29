from bisect import bisect_left
from typing import List


# Binary Search Min Answer
def earliestSecondToMarkIndices(
    nums: List[int], changeIndices: List[int]
) -> int:
    n, m = len(nums), len(changeIndices)
    if n > m:
        return -1

    def check(mx: int) -> bool:
        last_t = [-1] * n
        for t, idx in enumerate(changeIndices[:mx]):
            last_t[idx - 1] = t
        if -1 in last_t:
            return False

        cnt = 0
        for i, idx in enumerate(changeIndices[:mx]):
            idx -= 1
            if i == last_t[idx]:
                if nums[idx] > cnt:
                    return False
                cnt -= nums[idx]
            else:
                cnt += 1
        return True

    left = n + sum(nums)
    res = left + bisect_left(range(left, m + 1), True, key=check)
    return -1 if res > m else res


if __name__ == "__main__":
    nums = [2, 2, 0]
    changeIndices = [2, 2, 2, 2, 3, 2, 2, 1]
    assert earliestSecondToMarkIndices(nums, changeIndices) == 8
