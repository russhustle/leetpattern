from typing import List


# Brute Force
def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != m * n:
        return []
    array = []

    for i in range(m):
        row = original[n * i : n * (i + 1)]
        array.append(row)

    return array


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  Brute     |  O(m)  |  O(1)   |
# |------------|--------|---------|


original = [1, 2, 3, 4]
m = 2
n = 2

print(construct2DArray(original, m, n))  # [[1, 2], [3, 4]]
