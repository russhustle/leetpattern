from typing import List


def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[List[int]]:
    n = len(nums)
    res = []
    if n == 0:
        return [[lower, upper]]

    # start
    if nums[0] > lower:
        res.append([lower, nums[0] - 1])

    # middle
    for i in range(n - 1):
        if nums[i] + 1 < nums[i + 1]:
            res.append([nums[i] + 1, nums[i + 1] - 1])

    # end
    if nums[-1] < upper:
        res.append([nums[-1] + 1, upper])

    return res


def findMissingRangesCompact(nums: List[int], lower: int, upper: int) -> List[List[int]]:
    res = []

    for num in nums + [upper + 1]:
        if num > lower:
            res.append([lower, num - 1])
        lower = num + 1

    return res


if __name__ == "__main__":
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    assert findMissingRanges(nums, lower, upper) == [
        [2, 2],
        [4, 49],
        [51, 74],
        [76, 99],
    ]
    assert findMissingRangesCompact(nums, lower, upper) == [
        [2, 2],
        [4, 49],
        [51, 74],
        [76, 99],
    ]
