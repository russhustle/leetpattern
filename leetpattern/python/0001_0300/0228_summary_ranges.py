from typing import List


# Variable Sliding Window
def summaryRanges(nums: List[int]) -> List[str]:
    left, right = 0, 0
    n = len(nums)
    res = []

    while left < n:
        while right + 1 < n and nums[right] + 1 == nums[right + 1]:
            right += 1

        if left == right:
            res.append(f"{nums[left]}")
        else:
            res.append(f"{nums[left]}->{nums[right]}")

        right += 1
        left = right

    return res


if __name__ == "__main__":
    print(summaryRanges([0, 1, 2, 4, 5, 7]))
    # ["0->2", "4->5", "7"]
    print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    # ["0", "2->4", "6", "8->9"]
