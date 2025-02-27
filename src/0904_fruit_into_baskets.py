from collections import defaultdict
from typing import List


# Sliding Window Variable Size
def totalFruit(fruits: List[int]) -> int:
    n = len(fruits)
    if n <= 2:
        return n

    baskets = defaultdict(int)
    res, left = 0, 0

    for right in range(n):
        baskets[fruits[right]] += 1

        while len(baskets) > 2:
            baskets[fruits[left]] -= 1
            if baskets[fruits[left]] == 0:
                del baskets[fruits[left]]
            left += 1

        res = max(res, right - left + 1)

    return res


fruits = [1, 2, 3, 2, 2]
print(totalFruit(fruits))  # 4
