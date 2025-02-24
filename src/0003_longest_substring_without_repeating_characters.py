# Sliding Window - Variable
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n

    window = set()
    lp = 0
    res = 0

    for rp in range(n):
        while s[rp] in window:
            window.remove(s[lp])
            lp += 1
        window.add(s[rp])
        res = max(res, rp - lp + 1)

    return res


s = "abcabcbb"
assert lengthOfLongestSubstring(s) == 3
