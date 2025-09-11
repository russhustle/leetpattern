from collections import defaultdict


# Sliding Window Variable Max
def maximumLengthSubstring(s: str) -> int:
    n = len(s)
    if n <= 2:
        return n

    counts = defaultdict(int)
    left = 0
    res = 0

    for right in range(n):
        while left < right and counts[s[right]] == 2:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        res = max(res, right - left + 1)
        counts[s[right]] += 1

    return res


if __name__ == "__main__":
    s = "bcbbbcba"
    assert maximumLengthSubstring(s) == 4
