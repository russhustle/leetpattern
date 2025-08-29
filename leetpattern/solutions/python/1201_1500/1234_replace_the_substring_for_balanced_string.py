from collections import Counter


# Sliding Window Variable Min
def balancedString(s: str) -> int:
    n = len(s)
    m = n // 4
    counts = Counter(s)

    if len(counts) == 4 and min(counts.values()) == m:
        return 0

    left = 0
    res = float("inf")

    for right in range(n):
        counts[s[right]] -= 1

        while max(counts.values()) <= m:
            res = min(res, right - left + 1)
            counts[s[left]] += 1
            left += 1

    return res


if __name__ == "__main__":
    assert balancedString("QWER") == 0
    assert balancedString("QQWE") == 1
    assert balancedString("QQQW") == 2
    assert balancedString("QQQQ") == 3
