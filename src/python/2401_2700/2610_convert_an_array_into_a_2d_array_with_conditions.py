from collections import Counter
from typing import List


def findMatrix(nums: List[int]) -> List[List[int]]:
    counts = Counter(nums)
    res = []

    for num, freq in counts.items():
        while len(res) < freq:
            res.append([])

        for i in range(freq):
            res[i].append(num)

    return res


if __name__ == "__main__":
    nums = [1, 3, 4, 1, 2, 3, 1]
    print(findMatrix(nums))
    # [[1, 3, 4, 2], [1, 3], [1]]
