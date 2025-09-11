from functools import cache
from typing import List


# Memoization
def mostPoints(questions: List[List[int]]) -> int:
    @cache
    def dfs(i: int) -> int:
        if i >= len(questions):
            return 0
        return max(dfs(i + 1), dfs(i + questions[i][1] + 1) + questions[i][0])

    return dfs(0)


if __name__ == "__main__":
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    print(mostPoints(questions))  # 5
