from typing import List


# Greedy
def maximumHappinessSum(happiness: List[int], k: int) -> int:
    selected = 0
    happinessScore = 0
    happiness.sort(reverse=True)

    for score in happiness:
        if selected == k:
            return happinessScore
        happinessScore += max(0, score - selected)
        selected += 1

    return happinessScore


happiness = [1, 2, 3]
k = 2
print(maximumHappinessSum(happiness, k))  # 4
