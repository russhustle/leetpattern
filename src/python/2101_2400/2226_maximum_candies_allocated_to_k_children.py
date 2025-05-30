from typing import List


# Binary Search Max Answer
def maximumCandies(candies: List[int], k: int) -> int:
    def check(low):
        return sum(c // low for c in candies) >= k

    left, right = 0, max(candies) + 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid
        else:
            right = mid

    return left


# Binary Search Max Answer - Optimized
def maximumCandiesOptimized(candies: List[int], k: int) -> int:
    def check(low):
        return sum(c // low for c in candies) >= k

    # Use the minimum of max(candies) and sum(candies) // k to limit the search space
    left, right = 0, min(max(candies), sum(candies) // k) + 1

    while left + 1 < right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid
        else:
            right = mid

    return left


if __name__ == "__main__":
    candies = [5, 8, 6]
    k = 3
    assert maximumCandies(candies, k) == 5
    assert maximumCandiesOptimized(candies, k) == 5
