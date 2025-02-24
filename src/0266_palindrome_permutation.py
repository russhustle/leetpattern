from collections import defaultdict


# Hash
def canPermutePalindromeDict(s: str) -> bool:
    if len(s) == 1:
        return True

    count = defaultdict(int)

    for ch in s:
        if count[ch] == 1:
            count[ch] = 0
            continue
        count[ch] = 1

    return sum(count.values()) <= 1


# Set
def canPermutePalindromeSet(s: str) -> bool:
    if len(s) == 1:
        return True

    seen = set()

    for ch in s:
        if ch in seen:
            seen.remove(ch)
        else:
            seen.add(ch)

    return len(seen) <= 1


assert canPermutePalindromeDict("carerac") is True
assert canPermutePalindromeSet("carerac") is True
