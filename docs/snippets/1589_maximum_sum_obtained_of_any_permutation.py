from typing import List


# Greedy
def maxSumRangeQuery(nums: List[int], requests: List[List[int]]) -> int:
    n = len(nums)
    freq = [0 for _ in range(n + 1)]

    for start, end in requests:
        freq[start] += 1
        if end + 1 < n:
            freq[end + 1] -= 1

    for i in range(1, n):
        freq[i] += freq[i - 1]

    freq.pop()

    freq.sort(reverse=True)
    nums.sort(reverse=True)

    max_sum = 0
    mod = 10**9 + 7

    for i, j in zip(nums, freq):
        max_sum += i * j
        max_sum %= mod

    return max_sum


nums = [1, 2, 3, 4, 5]
requests = [[1, 3], [0, 1]]
print(maxSumRangeQuery(nums, requests))  # 19
