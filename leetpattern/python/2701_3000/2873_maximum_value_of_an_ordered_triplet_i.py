from typing import List


def maximumTripletValue(nums: List[int]) -> int:
    res, max_diff, pre_max = 0, 0, 0

    for num in nums:
        res = max(res, max_diff * num)
        max_diff = max(max_diff, pre_max - num)
        pre_max = max(pre_max, num)

    return res


if __name__ == "__main__":
    nums = [12, 6, 1, 2, 7]
    print(maximumTripletValue(nums))  # 77
