from typing import List


def LPS(pattern: str) -> List[int]:
    n = len(pattern)
    lps = [0 for _ in range(n)]
    j = 0

    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    return lps
