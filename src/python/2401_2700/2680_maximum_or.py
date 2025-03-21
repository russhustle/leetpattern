from typing import List


# Greedy
def maximumOr(nums: List[int], k: int) -> int:
    """Maximum OR of Array After k Operations

    Args:
        nums (List[int]): provided list of integers
        k (int): number of operations

    Returns:
        int: maximum OR of array after k operations
    """
    n = len(nums)
    suffix = [0 for _ in range(n)]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] | nums[i + 1]

    res, pre = 0, 0
    for num, suf in zip(nums, suffix):
        res = max(res, pre | (num << k) | suf)
        pre |= num

    return res


if __name__ == "__main__":
    print(maximumOr(nums=[8, 1, 2], k=2))  # 35
