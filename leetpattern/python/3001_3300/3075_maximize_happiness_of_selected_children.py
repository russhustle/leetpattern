from typing import List


class maximumHappinessSum:
    @staticmethod
    def greedy(happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        i = 0

        while i < k:
            if happiness[i] <= i:
                break
            res += happiness[i] - i
            i += 1

        return res


if __name__ == "__main__":
    assert maximumHappinessSum.greedy([1, 2, 3], 2) == 4
    assert maximumHappinessSum.greedy([5, 1, 3, 7], 3) == 12
