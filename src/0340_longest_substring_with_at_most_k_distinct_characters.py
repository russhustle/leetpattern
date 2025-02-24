from collections import defaultdict


# Sliding Window Variable
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    n = len(s)
    if n <= k:
        return n

    window = defaultdict(int)
    left, res = 0, 0

    for right in range(n):
        window[s[right]] += 1
        while len(window) > k:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        res = max(res, right - left + 1)

    return res


s = "eceba"
k = 2
assert lengthOfLongestSubstringKDistinct(s, k) == 3
