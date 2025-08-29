"""
-   Return the minimum number of candies you must give.
"""

from typing import List


# Greedy
def candy(ratings: List[int]) -> int:
    # TC: O(n)
    # SC: O(n)
    n = len(ratings)

    if n <= 1:
        return n

    candy = [1 for _ in range(n)]

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candy[i] = candy[i - 1] + 1

    for j in range(n - 2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            candy[j] = max(candy[j], candy[j + 1] + 1)

    return sum(candy)


ratings = [1, 0, 2]
print(candy(ratings))  # 5
