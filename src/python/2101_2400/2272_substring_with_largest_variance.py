from itertools import permutations
from math import inf
from string import ascii_lowercase


# DP State Machine
def largestVariance(s: str) -> int:
    res = 0

    for a, b in permutations(ascii_lowercase, 2):
        f0, f1 = 0, -inf
        for ch in s:
            if ch == a:
                f0 = max(f0, 0) + 1
                f1 += 1
            elif ch == b:
                f1 = f0 = max(f0, 0) - 1

            res = max(res, f1)
    return res


if __name__ == "__main__":
    s = "aababbb"
    print(largestVariance(s))  # 3
