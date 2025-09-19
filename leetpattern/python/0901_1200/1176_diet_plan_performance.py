from typing import List


# Sliding Window Fixed Size
def dietPlanPerformance(calories: List[int], k: int, lower: int, upper: int) -> int:
    res, T = 0, 0

    for i in range(len(calories)):
        T += calories[i]

        if i < k - 1:
            continue

        if T < lower:
            res -= 1
        elif T > upper:
            res += 1

        T -= calories[i - k + 1]

    return res


if __name__ == "__main__":
    calories = [1, 2, 3, 4, 5]
    k = 1
    lower = 3
    upper = 3

    assert dietPlanPerformance(calories, k, lower, upper) == 0
