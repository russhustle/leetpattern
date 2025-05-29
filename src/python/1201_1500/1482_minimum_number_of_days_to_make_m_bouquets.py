from typing import List


# Binary Search Min Answer
def minDays(bloomDay: List[int], m: int, k: int) -> int:
    n = len(bloomDay)
    if m * k > n:
        return -1

    def canMake(day: int) -> bool:
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    left, right = min(bloomDay), max(bloomDay)
    res = -1

    while left <= right:
        mid = left + (right - left) // 2
        if canMake(mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res


if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    assert minDays(bloomDay, m, k) == 3
