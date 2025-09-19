from itertools import accumulate
from typing import List


# Monotonic Stack
def totalStrength(strength: List[int]) -> int:
    n = len(strength)
    left = [-1 for _ in range(n)]
    right = [n for _ in range(n)]
    stack = []

    for i, v in enumerate(strength):
        while stack and strength[stack[-1]] >= v:
            right[stack.pop()] = i
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    prefix_sum = list(accumulate(accumulate(strength, initial=0), initial=0))

    ans = 0
    for i, v in enumerate(strength):
        l, r = left[i] + 1, right[i] - 1
        tot = (i - l + 1) * (prefix_sum[r + 2] - prefix_sum[i + 1]) - (r - i + 1) * (
            prefix_sum[i + 1] - prefix_sum[l]
        )
        ans += v * tot

    return ans % (10**9 + 7)


strength = [1, 3, 1, 2]
print(totalStrength(strength))  # 44
