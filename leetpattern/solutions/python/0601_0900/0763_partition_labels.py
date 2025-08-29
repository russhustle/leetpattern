from typing import List


# 1. Hashmap
def partitionLabels1(s: str) -> List[int]:
    hashmap = {}

    for i, j in enumerate(s):
        if j not in hashmap:
            hashmap[j] = [i, i]
        else:
            hashmap[j][1] = i

    intervals = list(hashmap.values())
    intervals.sort(key=lambda x: x[0])

    if len(intervals) < 2:
        return len(intervals)

    res = []
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
        else:
            res.append(intervals[i][0])

    res.append(intervals[-1][1] + 1)

    if len(res) == 1:
        return res
    else:
        for i in range(len(res) - 1, 0, -1):
            res[i] -= res[i - 1]
        return res


# Single Pass Partitioning
def partitionLabels2(s: str) -> List[int]:
    last = {c: i for i, c in enumerate(s)}
    res = []
    start, end = 0, 0

    for i, c in enumerate(s):
        end = max(end, last[c])
        if end == i:
            res.append(end - start + 1)
            start = i + 1

    return res


print(partitionLabels1("abaccd"))  # [3, 2, 1]
print(partitionLabels2("abaccd"))  # [3, 2, 1]
