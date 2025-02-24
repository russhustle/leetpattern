from collections import defaultdict


# Sliding Window - Variable
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    n = len(s)
    if n <= 2:
        return n

    window = defaultdict(int)
    lp, res = 0, 0

    for rp in range(n):
        window[s[rp]] += 1

        while len(window) > 2:
            window[s[lp]] -= 1
            if window[s[lp]] == 0:
                del window[s[lp]]
            lp += 1

        res = max(res, rp - lp + 1)

    return res


s = "ccaabbb"
assert lengthOfLongestSubstringTwoDistinct(s) == 5
