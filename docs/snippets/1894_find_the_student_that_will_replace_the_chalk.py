from typing import List


# Math
def chalkReplacer(chalk: List[int], k: int) -> int:
    total = sum(chalk)

    k %= total

    for i, c in enumerate(chalk):
        k -= c

        if k < 0:
            return i

    return -1


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |    Math    |  O(n)  |  O(1)   |
# |------------|--------|---------|


chalk = [5, 1, 5]
k = 22

print(chalkReplacer(chalk, k))  # 0
