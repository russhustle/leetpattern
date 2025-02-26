from typing import List


# Sliding Window Fixed Size
def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    n = len(customers)
    k = minutes
    if k >= n:
        return sum(customers)

    total_satisfied = sum(customers[i] for i in range(n) if not grumpy[i])

    cur, maxGrumpy = 0, 0

    for idx, customer in enumerate(customers):
        cur += customer if grumpy[idx] else 0

        if idx < k - 1:
            continue

        maxGrumpy = max(maxGrumpy, cur)

        cur -= customers[idx - k + 1] if grumpy[idx - k + 1] else 0

    return total_satisfied + maxGrumpy


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
print(maxSatisfied(customers, grumpy, minutes))  # 16
