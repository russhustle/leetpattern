from typing import List


def minSwaps(data: List[int]) -> int:
    n = len(data)
    total = sum(data)

    if total == 0 or total == 1 or total == n:
        return 0

    max_count = 0
    cur = 0
    left = 0

    for right in range(n):
        cur += data[right]

        if right - left + 1 > total:
            cur -= data[left]
            left += 1

        max_count = max(max_count, cur)

    return total - max_count


data = [1, 0, 1, 0, 1]
print(minSwaps(data))  # 1
