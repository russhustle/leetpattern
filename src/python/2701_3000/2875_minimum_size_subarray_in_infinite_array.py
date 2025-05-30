from typing import List


# Sliding Window Variable Min
def minSizeSubarray(nums: List[int], target: int) -> int:
    total = sum(nums)
    n = len(nums)
    div, mod = divmod(target, total)
    left, cur, res = 0, 0, float("inf")

    for right in range(n * 2):
        cur += nums[right % n]

        while cur > mod:
            cur -= nums[left % n]
            left += 1

        if cur == mod:
            res = min(res, right - left + 1)

    return res + div * n if res != float("inf") else -1


if __name__ == "__main__":
    assert minSizeSubarray([1, 2, 3], 5) == 2
    assert minSizeSubarray([1, 1, 1, 2, 3], 4) == 2
    assert minSizeSubarray([2, 4, 6, 8], 3) == -1
