from typing import List


def partitionArray(nums: List[int], k: int) -> int:
    nums.sort()
    mn = float("-inf")
    res = 0

    for num in nums:
        if num - mn > k:
            res += 1
            mn = num

    return res


if __name__ == "__main__":
    assert partitionArray([3, 6, 1, 2, 5], 2) == 2
