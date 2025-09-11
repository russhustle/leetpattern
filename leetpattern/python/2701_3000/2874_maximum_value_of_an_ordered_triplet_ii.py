from typing import List


def maximumTripletValue(nums: List[int]) -> int:
    res = 0
    max_diff = 0
    max_prev = 0

    for num in nums:
        res = max(res, max_diff * num)
        max_diff = max(max_diff, max_prev - num)
        max_prev = max(max_prev, num)

    return res


if __name__ == "__main__":
    nums = [12, 6, 1, 2, 7]
    print(maximumTripletValue(nums))  # 77
