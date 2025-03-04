from typing import List


# Stack
def buildArray(target: List[int], n: int) -> List[str]:
    res = []
    m, i, j = len(target), 1, 0

    while i <= n and j < m:
        res.append("Push")
        if target[j] != i:
            res.append("Pop")
        else:
            j += 1
        i += 1

    return res


target = [1, 3, 4]
n = 4
print(buildArray(target, n))
# ['Push', 'Push', 'Pop', 'Push', 'Push']
