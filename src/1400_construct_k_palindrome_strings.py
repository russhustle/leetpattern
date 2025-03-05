from collections import Counter


def canConstructCounter(s: str, k: int) -> bool:
    if len(s) < k:
        return False

    counts = Counter(s)
    odd = 0

    for c in counts.values():
        odd += c % 2

    return odd <= k


def canConstructHash(s: str, k: int) -> bool:
    if len(s) < k:
        return False

    counts = [0 for _ in range(26)]

    for ch in s:
        idx = ord(ch) - ord("a")
        if counts[idx] == 0:
            counts[idx] += 1
        else:
            counts[idx] -= 1

    return sum(counts) <= k


s = "annabelle"
k = 2
print(canConstructCounter(s, k))  # True
print(canConstructHash(s, k))  # True
