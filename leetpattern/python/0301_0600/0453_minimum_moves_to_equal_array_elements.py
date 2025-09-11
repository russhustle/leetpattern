from typing import List


def minMoves1(nums: List[int]) -> int:
    res, min_val = 0, min(nums)

    for num in nums:
        res += num - min_val

    return res


def minMoves2(nums: List[int]) -> int:
    return sum(nums) - len(nums) * min(nums)


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(minMoves1(nums))  # 3
    print(minMoves2(nums))  # 3
