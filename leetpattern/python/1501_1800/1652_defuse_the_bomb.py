"""
-   How to deal with the _circular array_?
    -   Trick: mod (index % length)
"""

from typing import List


# Sliding Window Fixed Size
def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)
    res = [0 for _ in range(n)]
    if k == 0:
        return res

    left, right = (1, k) if k > 0 else (n + k, n - 1)

    curSum = 0
    for i in range(left, right + 1):
        curSum += code[i % n]

    for i in range(n):
        res[i] = curSum

        curSum -= code[left % n]
        left += 1
        right += 1
        curSum += code[right % n]

    return res


code = [2, 4, 9, 3]
k = -2
print(decrypt(code, k))  # [12, 5, 6, 13]
