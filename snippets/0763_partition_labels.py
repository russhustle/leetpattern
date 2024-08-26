from typing import List


# 1. Hashmap
def partitionLabels1(s: str) -> List[int]:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
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

    result = []
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
        else:
            result.append(intervals[i][0])

    result.append(intervals[-1][1] + 1)

    if len(result) == 1:
        return result
    else:
        for i in range(len(result) - 1, 0, -1):
            result[i] -= result[i - 1]
        return result


# 2. Single Pass Partitioning
def partitionLabels2(s: str) -> List[int]:
    # Time complexity: O(n)
    # Space complexity: O(n)
    last = {c: i for i, c in enumerate(s)}

    start, end = 0, 0
    result = []

    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


print(partitionLabels1("abaccd"))  # [3, 2, 1]
print(partitionLabels2("abaccd"))  # [3, 2, 1]
