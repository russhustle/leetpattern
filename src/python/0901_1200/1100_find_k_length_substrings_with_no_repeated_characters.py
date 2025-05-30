from collections import defaultdict


# Sliding Window Fixed Size
def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    n = len(s)
    if k > n:
        return 0

    counts = defaultdict(int)
    res = 0

    for i, ch in enumerate(s):
        # add to the window
        counts[ch] += 1

        # form a valid window
        if i < k - 1:
            continue

        # update
        res += 1 if len(counts) == k else 0

        # remove from the window
        first = i - k + 1
        counts[s[first]] -= 1
        if counts[s[first]] == 0:
            del counts[s[first]]

    return res


if __name__ == "__main__":
    s = "havefunonleetcode"
    k = 5

    assert numKLenSubstrNoRepeats(s, k) == 6
